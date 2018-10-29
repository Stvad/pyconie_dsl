from __future__ import annotations
from typing import List, Dict, Set
from dataclasses import dataclass, field


@dataclass(frozen=True)
class Message:
    name: str = ""
    code: str = ""


class Event(Message):
    pass


class Action(Message):
    def execute(self):
        print(self)


@dataclass
class Transition:
    source: State
    destination: State
    trigger: Event


@dataclass
class State:
    name: str
    actions: List[Action] = field(default_factory=list)
    transitions: Dict[Event, Transition] = field(default_factory=dict)

    def add_transition(self, transition: Transition):
        self.transitions[transition.trigger] = transition

    def add_actions(self, *args):
        for action in args:
            self.actions.append(action)

    def handle(self, event):
        transition = self.transitions.get(event)
        return transition.destination if transition is not None else self


@dataclass
class StateMachine:
    initial_state: State
    current_state: State
    reset_events: Set[Event]

    def handle(self, event: Event):
        new_state = self.update_state(self.initial_state) if event in self.reset_events \
            else self.current_state.handle(event)
        self.update_state(new_state)

    def update_state(self, new_state):
        if new_state != self.current_state:
            print(f'Transitioning to {new_state}')
            self.current_state = new_state
            self.execute_actions()

    def execute_actions(self):
        for action in self.current_state.actions:
            action.execute()
