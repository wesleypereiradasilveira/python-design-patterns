import sqlite3
from typing import Any

class SingletonMetaclass(type):
    __instances = {}

    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        if self not in self.__instances:
            self.__instances[self] = super(SingletonMetaclass, self).__call__(*args, **kwargs)

        return self.__instances[self]
    
class Logger(type):
    pass
    
class Database(metaclass=SingletonMetaclass):
    connection = None

    def connect(self):
        if self.connection is None:
            print(f"No connection available")
            self.connection = sqlite3.connect("db.local")
            self.cursor = self.connection.cursor()

        return self.cursor
    