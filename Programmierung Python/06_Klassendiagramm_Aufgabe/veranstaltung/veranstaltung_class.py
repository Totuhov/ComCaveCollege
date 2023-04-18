class Veranstaltung:
    def __init__(self, name):
        self.name = name
        self.location = None
        self.art = None
        self.mitarbeiter = []

    def __str__(self):
        return f"\nVeranstaltung:({self.name}({self.location})({self.art})({self.mitarbeiter}))"
    
    def __repr__(self):
        return self.__str__()

    def setLocation(self, location):
        self.location = location
    
    def setArt(self, art):
        self.art = art
    
    def addMitarbeiter(self, mitarbeiter):
        self.mitarbeiter.append(mitarbeiter)