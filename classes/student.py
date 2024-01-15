
from classes.person import Person
from uuid import uuid4

class Student(Person):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.__registration = str(uuid4()).split("-")[0].upper()

    def make_money(self) -> None:
        print(f"How to make money?")
