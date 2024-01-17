
from rich import print as rprint

class Installer:
    def __init__(self, source, destination) -> None:
        self.options = []
        self.destination = destination
        self.source = source

    def preferences(self, choice):
        self.options.append(choice)

    def execute(self):
        for option in self.options:
            if list(option.values())[0]:
                rprint(f"Copying binaries from [yellow]{self.source}[/yellow] to [yellow]{self.destination}[/yellow]")
            else:
                rprint("[green]Operation finished[/green]")
