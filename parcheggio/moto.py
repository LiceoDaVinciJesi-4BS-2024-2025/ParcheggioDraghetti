#Nicolò Draghetti
#4 BS
#Moto

from veicolo import *

class Moto(Veicolo):
    
    def __init__(self, marca, modello, colore, cilindrata, alimentazione, targa, maxpasseggeri, npasseggeri):
        super().__init__(marca, modello, colore, cilindrata, alimentazione, targa)
        self.__maxpasseggeri = maxpasseggeri
        self.__passeggeri = passeggeri
