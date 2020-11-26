"""Define triggers to alter the state machine."""
from enum import Enum, auto


class Trigger(Enum):
    """Define triggers that can alter the state of the state machine."""
    CALL_DIALED = auto()
    HANG_UP = auto()
    CALL_CONNECTED = auto()
    PLACED_ON_HOLD = auto()
    TAKEN_OFF_HOLD = auto()
    LEFT_MESSAGE = auto()
