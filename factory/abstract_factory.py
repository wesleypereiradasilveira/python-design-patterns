
from abc import ABCMeta, abstractmethod

class PizzaFactory(metaclass=ABCMeta):
    @abstractmethod
    def create_vegan_pizza(self):
        pass

    @abstractmethod
    def create_pizza(self):
        pass

class BrazilianPizza(PizzaFactory):
    def create_vegan_pizza(self):
        return CassavaPizza()
    
    def create_pizza(self):
        return ShrimpPizza()
    
class ItalianPizza(PizzaFactory):
    def create_vegan_pizza(self):
        return BroccoliPizza()
    
    def create_pizza(self):
        return BolognesePizza()

class VeganPizza(metaclass=ABCMeta):
    @abstractmethod
    def prepare(self):
        pass

class Pizza(metaclass=ABCMeta):
    @abstractmethod
    def serve(self, VeganPizza):
        pass

class CassavaPizza(VeganPizza):
    def prepare(self):
        print(f"Preparing the {type(self).__name__}")

class ShrimpPizza(Pizza):
    def serve(self, VeganPizza):
        print(f"The {type(self).__name__} is served with shrimp on {type(VeganPizza).__name__}")

class BroccoliPizza(VeganPizza):
    def prepare(self):
        print(f"Preparing the {type(self).__name__}") 

class BolognesePizza(Pizza):
    def serve(self, VeganPizza):
        print(f"The {type(self).__name__} is served with {type(VeganPizza).__name__}")

class Pizzaria:
    def cook_pizzas(self):
        for factory in [BrazilianPizza(), ItalianPizza()]:
            self.factory = factory

            self.pizza = self.factory.create_pizza()
            self.vegan_pizza = self.factory.create_vegan_pizza()

            self.vegan_pizza.prepare()
            self.pizza.serve(self.vegan_pizza)
