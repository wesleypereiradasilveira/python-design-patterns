
from abc import ABCMeta, abstractmethod

class Factory:
    def create_speaking_animal(self, type):
        return eval(type)().speak()

class Animal(metaclass=ABCMeta):
    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        print("Au Au Au")

class Cat(Animal):
    def speak(self):
        print("Miau Miau Miau")

class Camel(Animal):
    def speak(self):
        print("It is hot lol")
        