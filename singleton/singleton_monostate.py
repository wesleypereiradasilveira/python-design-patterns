
from typing import Self

class SingletonMonostate:
    __state = {}

    def __new__(cls, *args, **kwargs) -> Self:
        obj = super(SingletonMonostate, cls).__new__(cls, *args, **kwargs)
        obj.__dict__ = cls.__state
        return obj
    