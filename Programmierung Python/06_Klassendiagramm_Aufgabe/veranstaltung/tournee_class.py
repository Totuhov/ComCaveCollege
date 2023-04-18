class Tournee:
    def __init__(self, name):
        self.name = name
        self.veranstaltungen = []

    def __str__(self):
        return f"Tournee({self.name}({self.veranstaltungen}))"
    
    def addVeranstaltung(self, veranstaltung, liste=False):
        if not liste:
            self.veranstaltungen.append(veranstaltung)
        else:
            self.veranstaltungen.extend(veranstaltung)
