
from command.complex_command import Action, Advisor, BuyOrder, SellOrder
from command.simple_command import Installer
from command.command import ConcreteCommand, Receiver, Invoker

def command_project_1():
    installer = Installer("python3.12.0.gzip", "/usr/bin/")
    installer.preferences({"python": True})
    installer.preferences({"java": False})
    installer.execute()

def command_project_2():
    receiver = Receiver()
    command = ConcreteCommand(receiver)
    invoker = Invoker()

    invoker.get_command(command)
    invoker.execute()

def command_project_3():
    action = Action()
    buy_order = BuyOrder(action)
    sell_order = SellOrder(action)

    advisor = Advisor()
    advisor.add_order(buy_order)
    advisor.add_order(sell_order)

