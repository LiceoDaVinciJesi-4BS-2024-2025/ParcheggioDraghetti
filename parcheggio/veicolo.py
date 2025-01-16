#Nicolò Draghetti
#4 BS
#Veicolo

marche = ["bmw", "porsche", "ferrari", "fiat", "nissan", "toyota", "maybach"]
colori = ["bianco", "nero", "blu", "rosso", "grigio", "arancione"]
alimentazioni = ["benzina", "diesel", "metano", "gpl", "ibrido"]
lettere = "QWERTYUIOPASDFGHJKLZXCVBNM"
numeri = "1234567890"

class Veicolo:
    
    def __init__(self, marca, modello, colore, cilindrata, alimentazione, targa):
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
    def cilindrata(self):
        return self.__cilindrata
    
    @cilindrata.setter
    def cilindrata(self, value):
        if value % 100 != 0:
            raise ValueError("")
        self.__cilindrata = value
        return

    @property
    def alimentazione(self):
        return self.__alimentazione
    
    @alimentazione.setter
    def alimentazione(self, value):
        if self.__alimentazione not in alimentazioni:
            raise ValueError("")
        self.__alimentazione = value
        return
    
    @property
    def targa(self):
        return self.__targa
    
    @cilindrata.setter
    def targa(self, value):
        if len(value) != 7 or value[0] not in lettere or value[1] not in lettere or value[2] not in numeri or value[3] not in numeri or value[4] not in numeri or value[5] not in lettere or value[6] not in lettere:
            raise ValueError("")
        self.__targa = value
        return
    
    def __lt__ (self, other):
        if self.__marca < other.__marca:
            return True
        elif self.__marca == other.__marca:
            if self.__modello < other.__modello:
                return True
            elif self.__modello == other.__modello:
                if self.__cilindrata < other.__cilindrata:
                    return True
        return False
