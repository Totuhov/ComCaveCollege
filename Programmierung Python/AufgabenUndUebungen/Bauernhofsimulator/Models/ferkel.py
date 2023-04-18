from Models.schwein import Schwein

class Ferkel(Schwein):

    ohrengroesse = None
    
    def __init__(self, name, farbe, gewicht, ohrengroesse):
        super().__init__(name, farbe, gewicht)
        self.ohrengroesse = ohrengroesse



