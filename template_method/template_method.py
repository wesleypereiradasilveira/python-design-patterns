
from rich import print as rprint
from abc import ABCMeta, abstractmethod

class Compiler(metaclass=ABCMeta):
    @abstractmethod
    def collect_source(self):
        ...

    @abstractmethod
    def compile_object(self):
        ...

    @abstractmethod
    def execute(self):
        ...

    def compile_execute(self):
        self.collect_source()
        self.compile_object()
        self.execute()

class IOS_Compiler(Compiler):
    def collect_source(self):
        rprint("Collecting [red]IOS[/red] source code...")

    def compile_object(self):
        rprint("Compiling [red]IOS[/red] source code to bytecode...")

    def execute(self):
        rprint("Executing the [red]IOS[/red] program on the environment...")

class Android_Compiler(Compiler):
    def collect_source(self):
        rprint("Collecting [green]Android[/green] source code...")

    def compile_object(self):
        rprint("Compiling [green]Android[/green] source code to bytecode...")

    def execute(self):
        rprint("Executing the [green]Android[/green] program on the environment...")

class AbstractClass(metaclass=ABCMeta):
    def __init__(self) -> None:
        ...

    @abstractmethod
    def operation_a(self):
        ...

    @abstractmethod
    def operation_b(self):
        ...

    def template_method(self):
        rprint("Defining the algorithm :: [blue]Operation A[/blue] after [yellow]Operation B[/yellow]")
        self.operation_b()
        self.operation_a()

class ConcreteClass(AbstractClass):
    def operation_a(self):
        rprint("Concrete [blue]Operation A[/blue]")

    def operation_b(self):
        rprint("Concrete [yellow]Operation B[/yellow]")

class Client:
    def main(self):
        self.concrete = ConcreteClass()
        self.concrete.template_method()
