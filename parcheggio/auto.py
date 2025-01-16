#Nicolò Draghetti
#4 BS
#Auto

from veicolo import *

class Auto(Veicolo):
    
    def __init__(self, marca, modello, colore, cilindrata, alimentazione, targa, maxpasseggeri, npasseggeri, maxmerce, merce):
        super().__init__(marca, modello, colore, cilindrata, alimentazione, targa)
        self.__maxpasseggeri = maxpasseggeri
        self.__passeggeri = passeggeri
        self.__maxmerce = maxmerce
        self.__merce = merce
