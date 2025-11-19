#Metodi Incapsulamento:

#Attributi Privati(__attributo) Proponendo due underscore al nome di attribruto , questo diventa privato , significa che non può essere
#accesso direttamente dall'esterno della classe. Per accedere o modificare un attributo privato si usano i metodi getter e setter

#Attributi Protetti(_attribuuto): Proponendo un underscore al nome di attributo , lo si considera protetto.
#Si tratta più di una convenzione che di una funzionalità linguistica, indicando che l'attributo debba essere usato solo all'interno della classe e delle sue sottoclassi

#Metodi Gettere e Setter: Metodi che permettono di ottere(get) o modificare(set) di attributi privati di una classe
#Offrono un controllo maggiore sull'accesso e sulla modifica dei dati

class Computer:
    def __init__(self):
        self.__processore = "Intel i5" #attributo privato
        
    def get_processore(self):
        return self.__processore
    
    def set_processore(self,processore):
        self.__processore = processore
        
pc = Computer()
print(pc.get_processore()) #accede all'attributo privato tramite il getter
pc.set_processore("AMD Ryzen 5")#modifica attributo privato tramite il setter
print(pc.get_processore())