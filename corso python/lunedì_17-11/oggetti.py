#in python è un modello progettuale, l'oggetto è la realizzazione concreta di quel momento progettuale

#le classi sono un'astrazione dei concetti del mondo reale,in python sono un modello per la creazione di oggetti

#un oggetto è un istanza di una classe ovvero una copia univoca della classe che le sue proprietà uniche
#le classi sono definite usando la parola chiave class , seguita dal nome classe. Possono contenere metodi e attributi

#gli attributi sono variabili associate a una classe , rappresentano le proprietà di un oggetto , gli attributi di classe sono condivisi tra tutte le istanze della classe

#I metodi sono funzioni assocciate a una classe e rappresentano il comportamento di un oggetto

class Automobile: #dichiaro la classe
    numero_di_ruote = 4 #attributo di classe
    def __init__(self, marca, modello): #metodo costruttore
        self.marca = marca #attributo di istanza
        self.modello = modello #attributo di istanza
    def stampa_info(self):
            print("L'automobile è una ", self.marca, self.modello) 
            
#il self è un paramentro che viene usato dal nome reale del oggetto

auto1 = Automobile("Fiat", "500")
auto2 = Automobile("Bmw", "X3")

auto1.stampa_info()
auto2.stampa_info()
print(auto1)


class Persona:
    def __init__(self,nome,eta):
        self.nome = nome
        self.eta = eta
        
    def __str__(self):
        return f"Persona(nome={self.nome})"
    
    
#il costruttore è un metodo speciale che viene invocato automaticamente al momento della creazione di un nuovo oggetto.
#__init serve ad inizializzare l'oggetto appena creato , impostando attributi e valori iniziali, __init__ accetta sempre almeno il paramentro selfe e accetta ulteriori parametri per la configurazione iniziale

#I metodi sono funzioni definite all'interno di una classe che operano sugli oggetti della classe stessa
#TIPI DI METODI:

#Metodi di istanza : Operano su un'istanza specifica e accedono ai dati dell'oggetto tramite self.
#Metodi di classe : Operano sulla classe e non su un'istanza specifica.Sono definiti usando il decoratore @classmethod e ricevono come primo parametro la classe(cls)
#Metodi statici: Funzioni legate alla classe ma che non operano ne sull'istanza ne sulla classe. Definiti con il decoratore @staticmethod


    class calcolatrice:
        
    @staticmethod
    def somma(a,b):
        return a + b
    
#uso del metodo statico senza creare un'istanza
risultato = calcolatrice.somma(5,3)

print(risultato)
#Output 8


#Il metodo mostra_numero_istanze è un metodo di classe e usa il decoratore #classmethod il paramentro cls rappresenta la classe stessa e permette di accedere ad attributi di classe

class Contatore:
    numero_istanza = 0
    def __init__(self):
        Contatore.numero_istanze += 1 
        
    classmethod
    def mostra_numero_istanze(cls):
        print(f"Sono state creare {cls.numero_istanze}istanze")
        
    c1 = Contatore()
    c2 = Contatore()
    
    Contatore.mostra_numero_istanze()
    #Output: Sono state create 2 istanze
    
    
 



