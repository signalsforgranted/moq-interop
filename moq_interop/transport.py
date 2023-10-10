from enum import IntEnum


class MoqTransport:
    """ MoqTransport is a primitive parser of the MoQ Transport specification
    """

    def __init__() -> None:
        pass

    def decode_message(self, message):
        pass


class MoqMessage(IntEnum):
    OBJECT = 0x0
    SETUP = 0x1
    SUBSCRIBE_REQUEST = 0x3
    SUBSCRIBE_OK = 0x4
    SUBSCRIBE_ERROR = 0x5
    ANNOUNCE = 0x6
    ANNOUNCE_OK = 0x7
    ANNOUNCE_ERROR = 0x8
    GOAWAY = 0x10


class MoqError(IntEnum):
    TERMINATED = 0x0
    GENERIC = 0x1
    UNAUTHORIZED = 0x2
    GOAWAY = 0x10
