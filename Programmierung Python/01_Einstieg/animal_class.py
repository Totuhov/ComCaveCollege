class Animal:
    #Attribute (Eigenschaften) - Hier deklarierte Attribute sind static!
    #public
    countLegs = 4
    countEyes = 2
    #private = __ - nicht öffentlich
    __age = None
    #protected = _ - nur im paket sichtbar
    _weight = None
    # Achtung! private und protected sind nur Benennungsregeln.
    # Es wird bei der Laufzeit nicht eingeschränkt.

    #Konstruktoren
    def __init__(self, age, weight, gender):
        self.__age = age
        self._weight = weight
        self.gender = gender #Instanz-Variable

    #Methoden (Operationen)
    def getAge(self):
        return self.__age
    
    #Klassenmethode (Static)
    @staticmethod
    def makeSound():
        print("Animal makes a sound")

    
    # Spezielle Methode für String-Represenation der Klasse
    def __str__(self):
        return f"Animal:({self.__age})({self._weight})({self.gender})"
    