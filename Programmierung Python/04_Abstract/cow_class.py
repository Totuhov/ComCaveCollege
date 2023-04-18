from animal_class import Animal

class Cow(Animal):
    def __str__(self):
        return f"Cow({self.legs}) - ({self.eyes})"
    
    def makeSound(self):
        print("Mooo!")