from typing import List, Dict

from state_machine.dsl.context_manager import NewEntriesContext, events_context, actions_context, create_state_context, \
    define_reset_events, TransitionStub
from state_machine.dsl.utils import load_module
from state_machine.model import State, Transition, StateMachine


def load_machine(path):
    module_dict = dict(globals())
    module_dict['events'], events = events_context(module_dict)
    module_dict['commands'], actions = actions_context(module_dict)

    states = {}
    transitions = []
    module_dict['state'] = create_state_context(module_dict, states, transitions)

    initial_state_container = {}
    initial_state_transitions = []
    module_dict['initial_state'] = create_state_context(module_dict, initial_state_container, initial_state_transitions)

    reset_events = []
    module_dict['reset_events'] = define_reset_events(reset_events)

    load_module(path, module_dict)
    load_transitions(transitions + initial_state_transitions, {**states, **initial_state_container})

    initial_state = next(iter(initial_state_container.values()))
    return StateMachine(initial_state, initial_state, reset_events)


def load_transitions(transitions: List[TransitionStub], states: Dict[str, State]):
    for transition_stub in transitions:
        states[transition_stub.initial_state.name].add_transition(
            Transition(transition_stub.initial_state, states[transition_stub.target_name], transition_stub.trigger))


print(load_machine(
    '/Users/sitalov/Dropbox/SoftwareEngineering/Experiments/Python/dsl/pyconie/state_machine/example_context_manager.py'))
