
from abc import ABCMeta, abstractmethod

class Command(metaclass=ABCMeta):
    def __init__(self, receiver) -> None:
        self.receiver = receiver

    @abstractmethod
    def execute(self):
        pass

class ConcreteCommand(Command):
    def __init__(self, receiver) -> None:
        self.receiver = receiver

    def execute(self):
        self.receiver.action()

class Receiver:
    def action(self):
        print("Receiver action")

class Invoker:
    def get_command(self, command):
        self.command = command

    def execute(self):
        self.command.execute()
