
class Actor:
    def __init__(self) -> None:
        self.ocupied = False

    def unavailable(self):
        self.ocupied = True
        print(f"{type(self).__name__} is ocupied")

    def available(self):
        self.ocupied = False
        print(f"{type(self).__name__} is available")

    def check_availability(self):
        return self.ocupied

class Agent:
    def work(self):
        actor = Actor()
        if actor.check_availability():
            actor.unavailable()
        else:
            actor.available()
