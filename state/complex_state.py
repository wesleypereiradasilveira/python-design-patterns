
from rich import print as rprint
from abc import ABCMeta, abstractmethod

class ComputerState(metaclass=ABCMeta):
    name: str = "state"
    is_allowed: list = []

    def change(self, state):
        if state.name in self.is_allowed:
            rprint(f"Current: [red]{self}[/red] => change state to: [green]{state.name}[/green]")
            self.__class__ = state
        else:
            rprint(f"Current: [red]{self}[/red] => couldn't be changed to: [green]{state.name}[/green]")

    def __str__(self) -> str:
        return self.name

class SwitchOn(ComputerState):
    name: str = "SwitchOn"
    is_allowed: list = ["SwitchOf", "SwitchOn", "Sleep"]

class SwitchOf(ComputerState):
    name: str = "SwitchOf"
    is_allowed: list = ["SwitchOn"]

class Sleep(ComputerState):
    name: str = "Sleep"
    is_allowed: list = ["SwitchOn"]

class Computer:
    def __init__(self, model: str = "Dell") -> None:
        self.mode = model
        self.state = SwitchOf()

    def change(self, state):
        self.state.change(state)
