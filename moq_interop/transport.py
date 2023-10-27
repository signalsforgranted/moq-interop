from enum import IntEnum

NOQ_ALPN = ["moq-00"]

class MoqTransport:
    """ MoqTransport is a primitive parser of the MoQ Transport specification
    """

    def __init__() -> None:
        pass

    def decode_message(self, message):
        pass


class MoqMessageType(IntEnum):
    OBJECT_WITH_PAYLOAD = 0x0
    OBJECT_WITHOUT_PAYLOAD = 0x2
    SUBSCRIBE = 0x3
    SUBSCRIBE_OK = 0x4
    SUBSCRIBE_ERROR = 0x5
    ANNOUNCE = 0x6
    ANNOUNCE_OK = 0x7
    ANNOUNCE_ERROR = 0x8
    UNANNOUNCE = 0x9
    UNSUBSCRIBE = 0xA
    SUBSCRIBE_FIN = 0xB
    SUBSCRIBE_RST = 0xC
    GOAWAY = 0x10
    CLIENT_SETUP = 0x40
    SERVER_SETUP = 0x41


class MoqError(IntEnum):
    NO_ERROR = 0x0
    GENERIC = 0x1
    UNAUTHORIZED = 0x2
    PROTOCOL_VIOLATION = 0x3
    GOAWAY = 0x10
