
from abc import ABCMeta, abstractmethod

class Wallet(metaclass=ABCMeta):
    @abstractmethod
    def pay(self) -> bool:
        pass

class Bank(Wallet):
    def __init__(self) -> None:
        self.card: int = 0
        self.account: int = 0

    def get_account(self) -> int:
        self.account = self.card
        return self.account
    
    def balance(self) -> bool:
        print(f"Bank: Checking if the account {self.get_account()} has balance")
        return True

    def set_card(self, card):
        self.card = card

    def pay(self) -> bool:
        if self.balance():
            print(f"Bank :: paying the bar")
            return True
        
        print(f"Sorry! you don't have enough balance to pay the bar")
        return False            

class DebitCard(Wallet):
    def __init__(self) -> None:
        self.bank = Bank()

    def pay(self) -> bool:
        card = input("Proxy :: Please, inform your card number: ")
        self.bank.set_card(card)
        return self.bank.pay()
    
class Client:
    def __init__(self) -> None:
        print(f"Client :: I want to buy a beer")
        self.debit_card = DebitCard()
        self.bought = False

    def paying(self) -> None:
        self.bought = self.debit_card.pay()

    def __del__(self) -> None:
        if self.bought:
            print(f"Client :: I could it pay and drink my beer")
        else:
            print(f"Client :: I would like to have more money to pay for the beer")
