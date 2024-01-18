

from state.complex_state import Computer, Sleep, SwitchOf, SwitchOn
from state.simple_state import ConcreteStateA, ConcreteStateB, Context

def state_project_1():
    context = Context()
    state_a = ConcreteStateA()
    state_b = ConcreteStateB()

    context.set_state(state_a)
    context.manage()

    context.set_state(state_b)
    context.manage()

def state_project_2():
    computer = Computer()
    computer.change(SwitchOn)
    computer.change(SwitchOf)
    computer.change(SwitchOn)
    computer.change(Sleep)
    computer.change(SwitchOf)
    computer.change(SwitchOn)
    computer.change(SwitchOf)
    computer.change(Sleep)