from animal_class import Animal

class Cat(Animal):
    def __init__(self, age, weight, gender, color):
        self.color = color
        # Aufruf des Konstruktors der Elternklasse mit weitegabe der Werte
        # super() zum ansprechen von Elementen aus der Elternklasse
        super().__init__(age, weight, gender)