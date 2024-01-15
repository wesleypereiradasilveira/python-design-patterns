
from typing import Any

class University(type):
    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        print(f"=== The args are: {args}")
        return type.__call__(self, *args, **kwargs)
    
class Geek(metaclass=University):
    def __init__(self, value_1, value_2) -> None:
        self.value_1 = value_1
        self.value_2 = value_2
        