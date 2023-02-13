from __future__ import annotations
import asyncio
from asyncio.events import AbstractEventLoop
from collections import defaultdict
from typing import (
    TYPE_CHECKING,
    Any,
    AsyncGenerator,
    Optional,
    Dict,
)
if TYPE_CHECKING:
    from .handler import TransportationHandler
    from .. import interfaces

from .token import Token
from . import exceptions


async def establish_connection(transporter: "TransportationHandler", host: str, port: int = 22606, loop: Optional["AbstractEventLoop"] = None) -> None:
    """
    Establish connection to provided host and port and assign ``<TransportationHandler>`` to it.
    """

    assert isinstance(loop, AbstractEventLoop) or loop is None, "<loop> must be an instance of AbstractEventLoop or None"
    __loop = loop if loop else asyncio.get_event_loop()
    try:
        await __loop.create_connection(lambda: transporter, host=host, port=port)
    except OSError:
        raise exceptions.EstablishConnectionError(host, port) from None


async def apply_iter(*cmd_tokens: Token[Any], return_exceptions: bool = False) -> AsyncGenerator[Any, None]:
    """
    Main interface for chunking the commands which need to be send to one or multiple testers at the same time.
    """
    aggregator: Dict["interfaces.IConnection", bytearray] = defaultdict(bytearray)
    queue: asyncio.Queue[asyncio.Future] = asyncio.Queue()
    for t in cmd_tokens:
        (data, fut) = await t.connection.prepare_data(t.request)
        aggregator[t.connection].extend(data)
        queue.put_nowait(fut)
    [c.send(r) for c, r in aggregator.items()]
    aggregator.clear()
    __excp_to_raise = None
    while not queue.empty():
        future = await queue.get()
        try:
            result_ = await future
        except Exception as e:
            if return_exceptions:
                yield e
            elif not __excp_to_raise:
                __excp_to_raise = e
        else:
            if not __excp_to_raise:
                yield result_
        queue.task_done()
    await queue.join()
    if __excp_to_raise:
        raise __excp_to_raise


async def apply(*cmd_tokens: Token[Any], return_exceptions: bool = False) -> list[Any]:
    """
    Main interface for chunking the commands which need to be send to one or multiple testers at the same time.
    """
    assert len(cmd_tokens) <= 200, "Number of the commands is bigger then 200 for one aggregation, please use function <apply_iter> instead"
    return [f async for f in apply_iter(*cmd_tokens, return_exceptions=return_exceptions)]
