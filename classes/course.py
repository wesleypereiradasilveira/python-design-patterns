
class Course:
    def __init__(self, name: str = "Standard Course", duration: int = 45) -> None:
        self.__name__ = name
        self.__duration = duration
