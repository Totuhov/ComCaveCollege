from abc import ABC
class Mitarbeiter(ABC):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Mitarbeiter:({self.name})"
    
    def __repr__(self):
        return self.__str__()
    