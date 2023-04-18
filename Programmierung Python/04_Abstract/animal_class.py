# Für Abstrakte Klassen muss das Modul für abstract base class (ABC) eingebunden werden
from abc import ABC, abstractmethod

class Animal(ABC):

    def __init__(self):
        self.legs = 4
        self.eyes = 2

    @abstractmethod
    def makeSound(self):
        pass

