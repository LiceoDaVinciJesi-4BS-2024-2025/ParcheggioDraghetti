#Nicolò Draghetti
#4 BS
#PostoMezzo

from veicolo import *
from datetime import datetime


tipi = ["auto", "moto"]

class PostoMezzo:
    
    def __init__(self, tipo:str, targa:str, libero:bool, partenza:datetime):
        self.__tipo = tipo
        self.__targa = targa
        self.__libero = libero
        self.__partenza = partenza
        
    def __str__(self):
        return "PostoMezzo: " + str(self.__dict__)
    
    @property
    def tipo(self):
        return self.__tipo
    
    @tipo.setter
    def tipo(self, value):
        if self.__tipo not in tipi:
            raise ValueError("")
        self.__tipo = value
        return
    
    @property
    def targa(self):
        return self.__targa
    
    @targa.setter
    def targa(self):
        self.__targa = veicolo.targa
        return
    
    @property
    def libero(self):
        return self.__libero
    
    @libero.setter
    def libero(self):
        if self.__targa == "":
            return True
        return False
    
    @property
    def partenza(self):
        return self.__partenza
    
    @partenza.setter
    def partenza(self, value):
        if self.__partenza < datetime.datetime.now():
            raise ValueError("")
        self.__partenza = value
        return
