from __future__ import annotations

from contextlib import contextmanager
from dataclasses import dataclass, field
from typing import List, Dict, Set

from state_machine.dsl.utils import iterable_of
from state_machine.model import Event, Action, State


@dataclass
class NewEntriesContext:
    module_dict: Dict
    action: function
    key_snapshot: Set = None

    def __enter__(self):
        self.key_snapshot = set(self.module_dict.keys())

    def __exit__(self, *args):
        defined = self.module_dict.keys() - self.key_snapshot
        print(defined)
        self.action(self.module_dict, defined)


def creation_context(module_dict, creator, container):
    def create_things(processed_dict, names):
        for name in names:
            created = creator(name, processed_dict[name])
            container.append(created)
            processed_dict[name] = created

    return NewEntriesContext(module_dict, create_things)


def events_context(module_dict):
    container = []
    return creation_context(module_dict, Event, container), container


def actions_context(module_dict):
    container = []
    return creation_context(module_dict, Action, container), container


def create_state_context(module_dict, state_container, transition_container: List):
    @contextmanager
    def state_context(state_name):
        result = State(state_name)
        state_container[state_name] = result

        stored_actions = module_dict.get('actions')
        module_dict['actions'] = result.add_actions

        stored_transitions = module_dict.get('transitions')
        transition_generator = TransitionGenerator(result)
        module_dict['transitions'] = transition_generator
        try:
            yield result
        finally:
            transition_container.extend(transition_generator.transition_stubs)

            module_dict['actions'] = stored_actions
            module_dict['transitions'] = stored_transitions

    return state_context


@dataclass
class TransitionStub:
    initial_state: State
    trigger: Event
    target_name: str


@dataclass
class TransitionGenerator:
    initial_state: State
    transition_stubs: List[TransitionStub] = field(default_factory=list)

    def __getitem__(self, transition_slices: List[slice]):
        for transition in iterable_of(transition_slices):
            self.transition_stubs.append(
                TransitionStub(self.initial_state, transition.start,
                               transition.stop))


def define_reset_events(container):
    def reset_events(*args):
        for event in args:
            container.append(event)

    return reset_events
