
from factory.simple_factory import Factory
from factory.factory_method import Linkedin, Facebook
from factory.abstract_factory import Pizzaria

def simple_factory() -> None:
    factory = Factory()
    animal = input("Which type of animal you want to create? [Dog, Cat, Camel] ")
    factory.create_speaking_animal(animal)

def factory_method() -> None:
    social_media = input("Which social media you want to create a profile? [Linkedin, Facebook] ")
    profile: Linkedin | Facebook = eval(social_media)()
    print(f"Creating the profile on {type(profile).__name__}")
    print(f"The profile has the following sections: {profile.get_sections()}")

def abstract_factory() -> None:
    pizzaria = Pizzaria()
    pizzaria.cook_pizzas()
    