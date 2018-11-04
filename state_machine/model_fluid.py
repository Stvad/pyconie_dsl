from __future__ import annotations

from dataclasses import dataclass
from uuid import uuid4

from state_machine.model import State, Event, Transition, StateMachine


@dataclass
class StateBuilder:
    state: State

    def on(self, trigger):
        return TransitionBuilder(self, trigger)

    def actions(self, *args):
        self.state.add_actions(*args)
        return self


@dataclass
class TransitionBuilder:
    state_builder: StateBuilder
    trigger: Event

    def transition_to(self, target: StateBuilder):
        constructed_state = self.state_builder.state
        constructed_state.add_transition(Transition(constructed_state, target.state, self.trigger))
        return self.state_builder


def state(name=None, actions=None):
    return StateBuilder(State(name=name or uuid4(), actions=actions or []))


def state_machine(*, initial_state: StateBuilder, reset_events):
    return StateMachine(initial_state.state, initial_state.state, reset_events)
