
class EventManager:
    def __init__(self) -> None:
        print("EventManager :: I'll start organizing \n")

    def organize(self):
        self.hall = PartyHall()
        self.hall.schedule()

        self.florist = Florist()
        self.florist.arranging_flowers()

        self.food = Restaurant()
        self.food.cook()

        self.music = Band()
        self.music.setup_stage()

class PartyHall:
    def __init__(self) -> None:
        print("PartyHall :: scheduling the party hall for the event \n")

    def is_available(self) -> bool:
        print("PartyHall :: This party hall is available? \n")
        return True

    def schedule(self) -> None:
        if self.is_available():
            print("PartyHall :: scheduled successfully for the event \n")

class Florist:
    def __init__(self) -> None:
        print("Florist :: Flowers for which occasion? \n")

    def arranging_flowers(self):
        print("Florist :: Roses, Daisies and Lilies will be used \n")

class Restaurant:
    def __init__(self) -> None:
        print("Restaurant :: cooking various dishes for the event \n")

    def cook(self):
        print("Restaurant :: Brazilian and Chinese food will be served \n")

class Band:
    def __init__(self) -> None:
        print("Music :: Music arrangements for the event \n")

    def setup_stage(self):
        print("Music :: setting up the stage to play jazz and rock in the event \n")

class Client:
    def __init__(self) -> None:
        print("Client :: Wow! preparations for the event! \n")

    def hire_event_manager(self):
        print("Client :: Hiring an event manager to organize the event \n")
        em = EventManager()
        em.organize()

    def __del__(self):
        print("Client :: It was very simple to organize the event with Facade \n")
        