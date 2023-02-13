from __future__ import annotations
import asyncio

from collections import (
    UserDict,
    defaultdict,
)
from functools import partialmethod
from typing import Any, Callable, Coroutine, Final
from .exceptions import (
    LostFuture,
    # BadStatus
)
from ..protocol.struct_response import Response
from ..protocol.exceptions import get_status_error

ON_EVT_DISCONNECTED: Final[int] = -1

CB = Callable[..., Coroutine[Any, None, None]]


class FuturesMapper(UserDict):
    data: dict[tuple[int, str], asyncio.Future]

    def make_future(self, req_id: int, cmd_name: str) -> asyncio.Future:
        fut = asyncio.Future()
        self.data[(req_id, cmd_name)] = fut
        return fut

    def pop_future(self, req_id: int, cmd_name: str) -> asyncio.Future:
        fut = self.data.pop((req_id, cmd_name), None)
        if not fut:
            raise LostFuture(req_id, cmd_name)
        return fut


class EventsObserver:

    __slots__ = ("__events",)

    def __init__(self) -> None:
        self.__events: dict[int, list[CB]] = defaultdict(list)

    def dispatch(self, evt: int, *args, **kwargs) -> None:
        for evt_func in self.__events.get(evt, []):
            asyncio.create_task(
                evt_func(*args, **kwargs)
            ).add_done_callback(self.__handle_exceptions)

    def __handle_exceptions(self, fut: asyncio.Future) -> None:
        if fut.cancelled():
            return None
        elif e := fut.exception():
            raise e

    def subscribe(self, evt: int, func: CB) -> None:
        self.__events[evt].append(func)


class ResponsePublisher:
    __slots__ = ("__futures_mapper", "__observer", "__logger")

    def __init__(self, logger) -> None:
        self.__logger = logger
        self.__futures_mapper = FuturesMapper()
        self.__observer = EventsObserver()

    def register_request(self, req_id: int, cmd_name: str) -> asyncio.Future:
        return self.__futures_mapper.make_future(req_id, cmd_name)

    def subscribe(self, evt: int, func: CB) -> None:
        self.__observer.subscribe(evt, func)

    subscribe_connection_lost = partialmethod(subscribe, ON_EVT_DISCONNECTED)

    def publish_connection_lost(self, info) -> None:
        self.__observer.dispatch(ON_EVT_DISCONNECTED, info)
        # self.__logger.debug(info)

    def publish_push_response(self, response: Response) -> None:
        self.__observer.dispatch(
            response.header.cmd_code,
            response
        )
        self.__logger.response_obj(response)

    def publish_param_response(self, response: Response) -> None:
        future = self.__futures_mapper.pop_future(
            req_id=response.header.request_identifier,
            cmd_name=response.class_name
        )
        if not response.is_ok:
            exception = get_status_error(response.command_status)  # type: ignore
            future.set_exception(exception(response.class_name))
        else:
            future.set_result(response.values)
        self.__logger.response_obj(response)
