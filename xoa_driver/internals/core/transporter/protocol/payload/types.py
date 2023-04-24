from __future__ import annotations
from ipaddress import (
    IPv4Address,
    IPv6Address,
)
from typing import (
    Any,
    NewType,
    Protocol,
    TypeVar,
)

FMT_ORDER_NETWORK = "!"
FMT_BYTES_STRING = "s"
FMT_SIG_CHAR = "b"
FMT_U_SIG_CHAR = "B"
FMT_LONG = "q"
FMT_U_LONG = "Q"
FMT_INT = "i"
FMT_U_INT = "I"
FMT_SHORT = "h"
FMT_U_SHORT = "H"

# region Base Type

GenericType = TypeVar("GenericType", covariant=True)

Hex = NewType('Hex', str)
"""Type aliace of string for indicate as string suppose to contain only valid HEX symbols"""


class XmpType(Protocol[GenericType]):
    __slots__ = ("data_format", "repetitions")

    repetitions: int | None
    data_format: str

    @staticmethod
    def client_format(val: Any) -> Any:
        return val

    @staticmethod
    def server_format(val: Any) -> Any:
        return val

# endregion


# region Xmp Types

class XmpByte(XmpType[int]):
    """Description class of XMP Byte type representation"""

    def __init__(self, *, signed: bool = False) -> None:
        self.data_format = FMT_SIG_CHAR if signed else FMT_U_SIG_CHAR
        self.repetitions = None


class XmpInt(XmpType[int]):
    """Description class of XMP Int type representation"""

    def __init__(self, *, signed: bool = True, climb: tuple[int, int] | None = None) -> None:
        self.data_format = FMT_INT if signed else FMT_U_INT
        self.repetitions = None


class XmpShort(XmpType[int]):
    """Description class of XMP Short type representation"""

    def __init__(self, *, signed: bool = True) -> None:
        self.data_format = FMT_SHORT if signed else FMT_U_SHORT
        self.repetitions = None


class XmpLong(XmpType[int]):
    """Description class of XMP Long type representation"""

    def __init__(self, *, signed: bool = True) -> None:
        self.data_format = FMT_LONG if signed else FMT_U_LONG
        self.repetitions = None


class XmpHex(XmpType[Hex]):
    """Description class of XMP Hex type representation"""

    def __init__(self, *, size: int | None = None) -> None:
        """
        if size is None means Hex string are not having a limit
        otherwise will use fixed size
        """
        self.data_format = FMT_BYTES_STRING
        self.repetitions = size

    @staticmethod
    def client_format(val: bytes) -> Hex:
        return Hex(val.hex())

    @staticmethod
    def server_format(val: Hex) -> bytes:
        return bytes.fromhex(val)


class XmpIPv6Address(XmpType[IPv6Address]):
    """Description class of XMP IPv6Address type representation"""

    def __init__(self) -> None:
        self.data_format = FMT_BYTES_STRING
        self.repetitions = 16

    @staticmethod
    def client_format(val: bytes) -> IPv6Address:
        return IPv6Address(val)

    @staticmethod
    def server_format(val: IPv6Address) -> bytes:
        return val.packed


class XmpIPv4Address(XmpType[IPv4Address]):
    """Description class of XMP IPv4Address type representation"""

    def __init__(self) -> None:
        self.data_format = FMT_BYTES_STRING
        self.repetitions = 4

    @staticmethod
    def client_format(val: bytes) -> IPv4Address:
        return IPv4Address(val)

    @staticmethod
    def server_format(val: IPv4Address) -> bytes:
        return val.packed


class XmpMacAddress(XmpHex):
    """Description class of XMP MacAddress type representation"""

    def __init__(self) -> None:
        self.data_format = FMT_BYTES_STRING
        self.repetitions = 6


class XmpStr(XmpType[str]):
    """Description class of XMP String type representation"""

    __slots__ = ("min_len",)

    def __init__(self, min_len: int | None = None) -> None:
        self.data_format = FMT_BYTES_STRING
        self.repetitions = None
        self.min_len = min_len

    @staticmethod
    def client_format(val: bytes) -> str:
        return val.partition(b'\0')[0].decode()

    @staticmethod
    def server_format(val: str) -> bytes:
        return val.encode()


class XmpSequence(XmpType[tuple]):
    """Description class of XMP Sequence type representation"""

    __slots__ = ("types_chunk", "length")

    def __init__(
        self,
        types_chunk: list[XmpByte | XmpInt | XmpShort | XmpLong | XmpHex | XmpIPv4Address | XmpIPv6Address | XmpMacAddress],
        length: int | None = None
    ) -> None:
        self.types_chunk = tuple(types_chunk)
        self.length = length
        self.repetitions = None
        self.data_format = "".join(f"{t.repetitions or ''}{t.data_format}" for t in self.types_chunk)

# endregion
