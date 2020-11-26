"""Define the rules governing the states and triggers that alter the state."""
from .trigger import Trigger
from .state import State

rules = {
    State.OFF_HOOK: [(Trigger.CALL_DIALED, State.CONNECTING)],
    State.CONNECTING: [
        (Trigger.HANG_UP, State.ON_HOOK),
        (Trigger.CALL_CONNECTED, State.CONNECTED),
    ],
    State.CONNECTED: [
        (Trigger.LEFT_MESSAGE, State.ON_HOOK),
        (Trigger.HANG_UP, State.ON_HOOK),
        (Trigger.PLACED_ON_HOLD, State.ON_HOLD),
    ],
    State.ON_HOLD: [
        (Trigger.TAKEN_OFF_HOLD, State.CONNECTED),
        (Trigger.HANG_UP, State.ON_HOOK),
    ]
}
