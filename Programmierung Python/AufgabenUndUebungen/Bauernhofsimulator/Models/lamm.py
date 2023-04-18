from Models.schaf import Schaf

class Lamm(Schaf):
    

    augenfarbe = None

    def __init__(self, name, farbe, gewicht, augenfarbe):
        super().__init__(name, farbe, gewicht)
        self.augenfarbe = augenfarbe