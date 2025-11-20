#il polimorfismo è un concetto chiave nella programmazione orientata agli oggetti(OOP)
#e permette di trattare oggetti di classe diverse attraverso un'interfaccia comune
#Il polimorfismo si manifesta principalemente tramite l'overriding dei metodi(Sovrascrittura)

#L'Overriding ci permette di utilizzare tutte e 3 le regole fondamentali insieme

#Overloading simulato : L'overloading ovvero la possibilità di avere più metodi nella stessa classe ma con differenti parametri, non è supportato da python
#ma è possibile simularlo usando argomenti opzionali o variadici

class Stampa:
    def mostra(self, a=None,b=None):
        if a is not None and b is not None:
            print(a + b)
        elif a is not None:
            print(a)
        else:
            print("Niente da mostrare")
            

#POLIMORFISMO ATTIVO: Si basa principalmente sul concetto di duck typing:
#Significa che non è necessario che un oggetto appartenga a una gerarchia di classi specifica o implementi un'interfaccia esplicita affinchè possa essere usato in maniera polimorfica
#basta che l'oggetto possieda i metodi o gli attributi necessari per l'operazione che si intende eseguire.

#esempio di polimorfismo duck typing , il tipo di polimorfismo più forte che abbiamo

class Cane:
    def parla(self):
        return "Bau!"
    
class Gatto:
    def parla(self):
        return"Miao!"

def fai_parlare(animale):
    print(animale.parla()) #non importa di che tipo sia l'aniamle
    
cane = Cane()
gatto = Gatto()

fai_parlare(cane) #output Bau!
fai_parlare(gatto) #output Miao!

            
#Esempio di ducktyping con ciclo polimorfico

class Cerchio:
    def disegna(self):
        print("Disegno un cerchio")

class Rettangolo:
    def disegna(self):
        print("Disegno un rettangolo")

def disegna_figura(figura):
    # Anche qui, basta che 'figura' abbia il metodo disegna
    figura.disegna()

# figure[0] = Cerchio() / figure[1] = Rettangolo()
figure = [Cerchio(), Rettangolo()]

# Iteriamo e disegniamo ogni figura
for figura in figure:
    disegna_figura(figura)

#seppure cerchio e rettangolo siano classi diverse , è possibile metterli in una lista e chiamare lo stesso metodo per ognuno senza controllare la classe appunto
#poichè entrami hanno il metodo disegna()

#Len(): è una funzione built-in , funziona con vari tipi di oggetti purchè questi implementino il metodo speciale __len__()

# __name = "__main__": è una condizione che si verifica se il modulo viene eseguito direttamente (e non importato da un altro script)
#Se è vero allora il blocco codice all'interno viene eseguito
#è una convenzione comune in python per distinguere tra codice esegubile direttamente e codice che viene importato come modulo

if __name__ == "__main":
    print("main")
else:
    print("import")
    
    