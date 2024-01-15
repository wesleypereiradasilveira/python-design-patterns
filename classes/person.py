
from abc import ABC, abstractclassmethod
from datetime import datetime

class Person(ABC):
    def __init__(self, name: str) -> None:
        self.__name = name
        self.__birth = datetime.now()

    def __str__(self) -> str:
        return self.__name
    
    def __repr__(self) -> str:
        return self.__name
    
    def make_money(self) -> None:
        pass
    