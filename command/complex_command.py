
from rich import print as rprint
from abc import ABCMeta, abstractmethod

# Command
class Order(metaclass=ABCMeta):
    @abstractmethod
    def execute(self):
        ...

# Concrete Commands
class BuyOrder(Order):
    def __init__(self, stock: str) -> None:
        self.stock = stock

    def execute(self):
        self.stock.buy()

class SellOrder(Order):
    def __init__(self, stock: str) -> None:
        self.stock = stock

    def execute(self):
        self.stock.sell()

# Receiver
class Action:
    def buy(self):
        rprint("[green]Buying[/green] stocks...")

    def sell(self):
        rprint("[red]Selling[/red] stocks...")

# Invoker
class Advisor:
    def __init__(self) -> None:
        self.__orders_queue: list = []

    def add_order(self, order: Order):
        self.__orders_queue.append(order)
        order.execute()
