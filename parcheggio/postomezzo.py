#Nicolò Draghetti
#4 BS
#PostoMezzo

tipi = ["auto", "moto"]

class PostoMezzo:
    
    def __init__(self, tipo, targa, libero, partenza):
        self.__tipo = tipo
        self.__targa = targa
        self.__libero = libero
        self.__partenza = partenza
        
    def __str__(self):
        return "PostoMezzo: " + str(self.__dict__)
