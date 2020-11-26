"""
Implement an example of the state system.
Demonstrating a single phone call.
"""
from state_machine import State, rules

if __name__ == '__main__':
    # Define a starting state (Gonna make a phone call)
    state = State.OFF_HOOK
    # Define exit state as we only implementing a single phone call.
    # State.ON_HOOK ends the call.
    exit_state = State.ON_HOOK

    # Keep looping until the phone is on the hook. On the hook ends the call.
    while exit_state != state:
        # We going to stage a phone call hence the phone is on the hook.
        print(f'The phone is currently {state}')

        # Find all possible triggers in the current state.
        for item in range(len(rules[state])):
            trigger = rules[state][item][0]
            print(f'{item}: {trigger}')
        idx = int(input('Select a trigger: '))
        state = rules[state][idx][1]

    print(f'Until the next phone call.... {state}')
