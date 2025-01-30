#Nicolò Draghetti
#4 BS
#Esercizio Parcheggio

from veicolo import *
from postomezzo import *
from datetime import datetime
class Parcheggio:
    def __init__(self):
        self.__postiauto = 1000
        self.__postimoto = 200
        self.__guadagnotot = 0
        
    def __str__ (self):
        return "Parcheggio" + str(self.__dict__)
    
    @property
    def postiauto(self):
        return self.__postiauto
    
    @property
    def postimoto(self):
        return self.__postimoto
    
    def prenotaposto(self, tipo):
        
        if postomezzo.tipo == "auto" and self.__postiauto > 0:
            self.__tipo = "auto"
            self.__targa = veicolo.targa
            self.__durata = postomezzzo.partenza - datetime.datetime.now()
            oreoccupazione = int(self.__durata.total_seconds()) // 3600
            pagamento = 1.5 * oreoccupazione
            self.__guadagnotot += pagamento
            file = open("park.data", a)
            file.write("Guadagno raggiunto: ", self.__guadagnotot)
            file.close()
            self.__postiauto -= 1
            file = open("park.data", a)
            file.write("Posti auto occupati: ", 1000 - self.__postiauto)
            file.close()
    
        if postomezzo.tipo == "moto" and self.__postimoto > 0:
            self.__tipo = "moto"
            self.__targa = veicolo.targa
            self.__durata = postomezzzo.partenza - datetime.datetime.now()
            oreoccupazione = int(self.__durata.total_seconds()) // 3600
            pagamento = 1.2 * oreoccupazione
            self.__guadagnotot += pagamento
            file = open("park.data", a)
            file.write("Guadagno raggiunto: ", self.__guadagnotot)
            file.close()
            self.__postimoto -= 1
            file = open("park.data", a)
            file.write("Posti moto occupati: ", 200 - self.__postimoto)
            file.close()
    
        if (postomezzo.tipo == "auto" and self.__postiauto == 0) or (postomezzo.tipo == "moto" and self.__postimoto == 0):
            raise ValueError("")
