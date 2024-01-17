
from rich import print as rprint
from abc import ABCMeta, abstractmethod

class Trip(metaclass=ABCMeta):
    @abstractmethod
    def departure(self):
        ...

    @abstractmethod
    def day_1(self):
        ...

    @abstractmethod
    def day_2(self):
        ...

    @abstractmethod
    def day_3(self):
        ...

    @abstractmethod
    def back_home(self):
        ...

    def route(self):
        self.departure()
        self.day_1()
        self.day_2()
        self.day_3()
        self.back_home()

class TripItaly(Trip):
    def departure(self):
        rprint("[green]Italy[/green] :: Airplane Trip...")

    def day_1(self):
        rprint("[green]Italy[/green] :: Visit the historical church")

    def day_2(self):
        rprint("[green]Italy[/green] :: Visit Veneza")

    def day_3(self):
        rprint("[green]Italy[/green] :: Enjoy Italian food in a good restaurant")

    def back_home(self):
        rprint("[green]Italy[/green] :: Back home with Airplane Trip...")

class TripArgentina(Trip):
    def departure(self):
        rprint("[blue]Argentina[/blue] :: Bus Trip...")

    def day_1(self):
        rprint("[blue]Argentina[/blue] :: Visit the historical obelisk")

    def day_2(self):
        rprint("[blue]Argentina[/blue] :: Visit Buenos Aires")

    def day_3(self):
        rprint("[blue]Argentina[/blue] :: Enjoy wine and meat in a good restaurant")

    def back_home(self):
        rprint("[blue]Argentina[/blue] :: Back home with Bus Trip...")

class GeekTravel:
    def prepare_trip(self):
        option = input("Where you want to go? [Italy, Argentina] ")
        if option.capitalize() == "Italy":
            self.trip = TripItaly()
            self.trip.route()
        elif option.capitalize() == "Argentina":
            self.trip = TripArgentina()
            self.trip.route()
        else:
            rprint(f"Sorry, we can go to [red]{option}[/red] yet.")
