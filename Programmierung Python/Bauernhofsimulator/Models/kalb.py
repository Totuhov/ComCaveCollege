from Models.kuh import Kuh

class Kalb(Kuh):
    flechengroesse = None
    
    def __init__(self, name, farbe, gewicht, flechengroesse):
        super().__init__(name, farbe, gewicht)
        self.flechengroesse = flechengroesse
