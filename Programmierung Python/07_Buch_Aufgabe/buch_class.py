class Buch:
    def __init__(self,titel,autor,verlag,seiten):
        self.__titel = titel
        self.__autor = autor
        self.__verlag = verlag
        self.__seiten = seiten
    
    def __str__(self):
        return f"Buch:({self.__titel}),({self.__autor}),({self.__verlag}),({self.__seiten}))"
    
    def __repr__(self) -> str:
        return self.__str__()
    
    def getTitel(self):
        return self.__titel
    
    def getAutor(self):
        return self.__autor
    
    def getVerlag(self):
        return self.__verlag
    
    def getSeiten(self):
        return self.__seiten