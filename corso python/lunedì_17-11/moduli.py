#I moduli permettono di organizzare il codice in unità logiche e riutilizzabili migliorando la modularità, la manutenibilità e la leggibilità del codice

#supponiamo di avere un file chiamato mio_modulo.py

def saluta(nome):
    print("Ciao,",nome)
    
PI = 3.14159

class Cerchio:
    def __init__(self,raggio):
        self.raggio = raggio
        
    def area(self):
        return PI * self.raggio**2
        
        
#ora possiamo importare il modulo mio_modulo in un altro programma python usando l'istruzione import

import mio_modulo

mio_modulo.saluta("Alice")

raggio = 2
cerchio = mio_modulo.Cerchio(raggio)
print(cerchio.area())