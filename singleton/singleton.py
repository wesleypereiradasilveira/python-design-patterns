
from typing import Self

class Singleton:
    __instance = None
    
    def __new__(cls) -> Self:
        if not hasattr(cls, "instance"):
            cls.instance = super(Singleton, cls).__new__(cls)
            print(f"Creating the object {cls.instance}")
        
        return cls.instance
    
    def __init__(self) -> None:
        if not Singleton.__instance:
            print("The method __init__ was called...")
            return None
        
        print(f"The instance has been created: {self.get_instance()}")

    @classmethod
    def get_instance(cls) -> Self:
        if not cls.__instance:
            cls.__instance = Singleton()

        return cls.__instance
    
class SanityCheck:
    __instance = None

    def __new__(cls, *args, **kwargs) -> Self:
        if not SanityCheck.__instance:
            SanityCheck.__instance = super(SanityCheck, cls).__new__(cls, *args, **kwargs)

        return SanityCheck.__instance
    
    def __init__(self) -> None:
        self.__servers = []

    def server_check(self, server) -> None:
        print(f"Checking: {self.__servers[server]}")

    def add_server(self) -> None:
        self.__servers.append("Server 1")
        self.__servers.append("Server 2")
        self.__servers.append("Server 3")
        self.__servers.append("Server 4")

    def change_server(self) -> None:
        self.__servers.pop()
        self.__servers.append("Server 5")
