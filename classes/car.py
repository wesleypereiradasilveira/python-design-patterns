
from classes.person import Person

class Car:
    def __init__(self, is_sedan: bool = False) -> None:
        self.__is_sedan = is_sedan
        self.__speed = 0
        self.__driver = None

    def __str__(self) -> str:
        if self.__driver:
            return f"This car belgons to {self.__driver}"
        
        return "Car without driver"
    
    def drive(self, driver: Person) -> None:
        self.__driver = driver
        self.acelerate(1)

    def acelerate(self, speed: int) -> None:
        self.__speed += speed

    def stop(self) -> None:
        self.__speed = 0
