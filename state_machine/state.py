"""Define the possible states of the state machine."""
from enum import Enum, auto


class State(Enum):
    """Define possible states of the state machine."""
    OFF_HOOK = auto()
    CONNECTING = auto()
    CONNECTED = auto()
    ON_HOLD = auto()
    ON_HOOK = auto()
