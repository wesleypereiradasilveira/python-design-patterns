
from abc import ABCMeta, abstractmethod

class Section(metaclass=ABCMeta):
    @abstractmethod
    def __repr__(self) -> str:
        pass

class PersonalSection(Section):
    def __repr__(self) -> str:
        return "Personal Section"
    
class AlbumSection(Section):
    def __repr__(self) -> str:
        return "Album Section"
    
class ProjectSection(Section):
    def __repr__(self) -> str:
        return "Project Section"
    
class PublishSection(Section):
    def __repr__(self) -> str:
        return "Publish Section"

class Profile(metaclass=ABCMeta):
    def __init__(self) -> None:
        self.sections = []
        self.create_profile()

    @abstractmethod
    def create_profile(self):
        pass

    def get_sections(self) -> list:
        return self.sections
    
    def add_section(self, section: Section) -> None:
        self.sections.append(section)

class Linkedin(Profile):
    def create_profile(self):
        self.add_section(PersonalSection())
        self.add_section(ProjectSection())
        self.add_section(PublishSection())

class Facebook(Profile):
    def create_profile(self):
        self.add_section(PersonalSection())
        self.add_section(AlbumSection())
        