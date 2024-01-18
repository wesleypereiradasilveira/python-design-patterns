
from rich import print as rprint
from abc import ABCMeta, abstractmethod

class State(metaclass=ABCMeta):
    @abstractmethod
    def manage(self):
        ...

class ConcreteStateA(State):
    def manage(self):
        rprint(f"[red]{type(self).__name__}[/red]")

class ConcreteStateB(State):
    def manage(self):
        rprint(f"[green]{type(self).__name__}[/green]")

class Context(State):
    def __init__(self) -> None:
        self.state: State = None

    def get_state(self) -> State:
        return self.state
    
    def set_state(self, state: State) -> None:
        self.state = state

    def manage(self) -> None:
        self.state.manage()
