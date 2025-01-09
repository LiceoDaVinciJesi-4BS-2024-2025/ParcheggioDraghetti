#Nicolò Draghetti
#4 BS
#Veicolo

class Veicolo:
    
    def __init__(self, marca, modello, colore, cilindrata(int), alimentazione, targa):
        self.__marca = marca
        self.__modello = modello
        self.__colore = colore
        self.__cilindrata = cilindrata
        self.__alimentazione = alimentazione
        self.__targa = targa
    
    def __str__(self):
        return "Veicolo: " + str(self.__dict__)
    
    @property
    def marca(self):
        return self.__marca

    @marca.setter
    def marca(self, value):
        if self.__marca not in marche:
            raise ValueError("")
        self.__marca = value
        return

    @property
    def modello(self):
        return self.__modello
    
    @property
    def colore(self):
        return self.__colore
    
    @colore.setter
    def colore(self, value):
        if self.__colore not in colori:
            raise ValueError("")
        self.__colore = value
        return

    @property
    def cilindra(self):
        return self.__cilindrata
    
    @cilindrata.setter
    def cilindrata(self, value):
        if value % 100 != 0:
            raise ValueError("")
        self.__cilindrata = value
        return
#
    @property
    def perimetro(self):
        return (self.__base + self.__altezza) * 2