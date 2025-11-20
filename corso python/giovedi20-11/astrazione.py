#capacità di nascondere i dettaglia completi da quelle che sono le funzioni essenziali

#le classi astratte sono delle classi che non posso diventare oggetti
#i metodi definiti all'interno di una classe astratta , devono essere implementati nelle classi derivate che ereditano dalla classe astratta

#prova astrazione:

from abc import ABC, abstractmethod

class Animale(ABC): #classe astratta che definsce
    @abstractmethod
    def muovi(self): #un metodo astratto muovi()
        pass

class Cane(Animale): #classe concreta che eredita da animale e implementa il metodo muovi()
    def muovi(self):
        print("Corro")
        
class Pesce(Animale): #classe concreta che eredita da animale e implementa il metodo muovi()
    def muovi(self):
        print
        ("Nuoto")
        
#Animale e Pesce sono una classe concreta che eredita da animale e implementa il metodo muovi()
#questo si assicura che ogni sottoclasse di Animale abbia il proprio modo di muoversi
#ma i dettagli Corro e Nuoto sono astratti 


#La libreria ABC fornisce una meccanismo per definire le classi astratte.
#questo modulo situato in collections.abc e abc , è utile per imporre un'interfaccia comune tra classi diverse

#@abstractmethod decoratore chiave che impone alle sottoclassi di implementare determinati metodi.
#oltre ai metodi astratti è possibile definire metodi concreti nelle classi astratte, offrendo un comportamento di base riutilizzabile

#ancora una volta python segue il ducktyping

