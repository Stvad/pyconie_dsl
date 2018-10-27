from __future__ import annotations

from contextlib import contextmanager
from dataclasses import dataclass, field
from typing import List, Dict, Set

from state_machine.model import Event, Action, State, Transition


@contextmanager
def events():
    keys = set(globals().keys())
    try:
        yield
    finally:
        print(globals().keys() - keys)
        defined = globals().keys() - keys

        for name in defined:
            globals()[name] = Event(name, globals()[name])



@dataclass
class EventsContext:
    module_dict: Dict
    key_snapshot: Set = None

    def __enter__(self):
        self.key_snapshot = set(self.module_dict.keys())
        print(self.module_dict)

    def __exit__(self, *args):
        defined = self.module_dict.keys() - self.key_snapshot
        print(defined)
        print(self.module_dict)

        for name in defined:
            self.module_dict[name] = Event(name, self.module_dict[name])

def events():
    keys = set(globals().keys())
    try:
        yield
    finally:
        print(globals().keys() - keys)
        defined = globals().keys() - keys

        for name in defined:
            globals()[name] = Event(name, globals()[name])

        # todo add to some container?


@contextmanager
def commands():
    # print(globals())
    keys = set(globals().keys())
    try:
        yield 5
    finally:
        print(globals().keys() - keys)
        defined = globals().keys() - keys

        for name in defined:
            globals()[name] = Action(name, globals()[name])


@contextmanager
def state(state_name, initial=False):
    result = State(state_name)
    globals()[state_name] = result

    stored_actions = globals().get('actions')
    globals()['actions'] = result.add_actions

    stored_transitions = globals().get('transitions')
    transition_generator = TransitionGenerator(result)
    globals()['transitions'] = transition_generator
    try:
        yield result
    finally:
        result.transitions = transition_generator.transition_stubs

        globals()['actions'] = stored_actions
        globals()['transitions'] = stored_transitions
        print(result)


def initial_state(state_name):
    return state(state_name, True)


@dataclass
class TransitionGenerator:
    initial_state: State
    transition_stubs: List[Transition] = field(default_factory=list)

    def __getitem__(self, transition_slices: List[slice]):
        for transition in transition_slices:
            self.transition_stubs.append(
                Transition(self.initial_state, None, transition.start))  # todo need to init transitions later?


def reset_events(*args):
    pass


# Dummies to help with syntax/completion/etc

transitions = []


def actions(*args):
    pass
