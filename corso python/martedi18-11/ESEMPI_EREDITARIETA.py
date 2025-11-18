#l'ereditarietà permette ad una classe figlio (detta sottoclasse) di ereditare attributi e metodi da un'altra classe padre(superclasse)
#ogni classe padre può avere infinite classe figlio , ogni classe figlio può avere più classe padre 

#super() permette di richiamare il costruttore della super classe
#permettendo alla sottoclasse di estendere o modificare il comportamento della superclasse()
#si usa anche per accedere ai metodi della superclasse che sono stati sovrascritti nelle sottoclasse

#Sovrascrittura di metodi: la sottoclasse può sovrascrivere i metodi della superclasse per modificare o estendere il loro comportament.
#utile quando si vuole che una sottoclasse si comporti in modo leggermente diverso rispetto alla superclasse

#Ereditarietà multipla: in python una sottoclasse può ereditare da più superclasse.
#si può realizzare elecando le superclasses tra parentesi durante la definizione delle sottoclassi


## Classe base
class Animale:
    def __init__(self, nome):
        self.nome = nome

    def parla(self):
        print(f"{self.nome} fa suono generico.")

# Classe derivata (eredita da Animale)
class Cane(Animale):
    def parla(self):
        print(f"{self.nome} abbaia!")


animale_generico = Animale("AnimaleGenerico")
cane = Cane("Fido")

animale_generico.parla()  # Output: AnimaleGenerico fa suono generico.
cane.parla()               # Output: Fido abbaia!


#ESEMPIO MULTIEREDITARIETA'

class Veicolo:
    def __init__(self,marca,modello):
        self.marca = marca
        self.modello = modello
        
        
    def mostra_informazioni(self):
        print(f"Veicolo marca {self.marca}, modello {self.modello}")
        
        
class DotazioniSpeciali:
    def __init__(self, dotazioni):
        self.dotazioni = dotazioni
        
    def mostra_dotazioni(self):
        print(f"Dotazioni speciali:{','.join(self.dotazioni)}")
        
#Ora creamo una classe AutomobileSportiva che eredita sia da Veicolo che da DotazioniSpeciali, dimostrando l'ereditarietà multipla
#usermo super() per chiamare i costruttori delle classibase e sovrascriveremo il metodo mostra_informazioni per aggiungere ulteriori dettagli specifici dell'AutomobileSportiva


class AutomobileSportiva(Veicolo, DotazioniSpeciali):
    def __init__(self, marca, modello, dotazioni, cavalli):
        Veicolo.__init__(self, marca, modello) #Alternativa a super() per l'ereditarietà multipla
        DotazioniSpeciali.__init__(self, dotazioni)
        self.cavalli = cavalli

    def mostra_informazioni(self):
        super().mostra_informazioni() # Chiamiamo il metodo della prima superclasse
        print(f"Potenza: {self.cavalli} CV")
        self.mostra_dotazioni()
        #Possiamo chiamare metodi di entrambe le superclassi
