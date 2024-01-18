
from rich import print as rprint

class Model:
    def __init__(self) -> None:
        self.products: dict = {
            "ps5": {
                "id": 1,
                "name": "Playstation 5",
                "price": 1244
            },
            "xbox": {
                "id": 2,
                "name": "Xbox",
                "price": 1445
            },
            "switch": {
                "id": 3,
                "name": "Nintendo Switch",
                "price": 1567
            }
        }

class Controller:
    def __init__(self) -> None:
        self.model: Model = Model()

    def list_products(self) -> None:
        products = self.model.products.keys()

        rprint("[blue]---------- Products ----------[/blue]")
        for product in products:
            rprint(f"[green]Id: [/green]{self.model.products[product]['id']}")
            rprint(f"[green]Name: [/green]{self.model.products[product]['name']}")
            rprint(f"[green]Price: [/green]{self.model.products[product]['price']} \n")

class View:
    def __init__(self) -> None:
        self.controller: Controller = Controller()

    def products(self) -> None:
        self.controller.list_products()
