#Metodi Incapsulamento: #concetto di programmazione orientata agli oggetti che raggruppa dati (attributi) e metodi all'interno di una classe, proteggendo i dati da accessi esterni non autorizzati

#Attributi Privati(__attributo) Proponendo due underscore al nome di attribruto , questo diventa privato , significa che non può essere
#accesso direttamente dall'esterno della classe. Per accedere o modificare un attributo privato si usano i metodi getter e setter

#Attributi Protetti(_attribuuto): Proponendo un underscore al nome di attributo , lo si considera protetto.
#Si tratta più di una convenzione che di una funzionalità linguistica, indicando che l'attributo debba essere usato solo all'interno della classe e delle sue sottoclassi

#Metodi Getter e Setter: Metodi che permettono di ottere(get) o modificare(set) di attributi privati di una classe
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


#I livelli di visibilità sono concetti importanti per gestire accesso e visibilità della variabile in differenti parti del codice
#I principali livelli sono :

#Globale: Una variabile dichiarata fuori da tutte le funzioni è conosciuta come variabile globale.
#E' accessibile da qualsiasi punto del codice dello stesso modulo , incluso dentro le funzioni , a meno che non venga oscurata da una variabile locale con lo stesso nome



#Locale: Le variabili dichiarate all'interno di una funzione e sono accessibili all'interno di quella funzione


#Non-Locale: Si applica nelle funzioni annidate, dove una variabile deve essere accessibile in più di una funzione interna ma non globalemente. Si usa la parola chiave nonlocal


# Variabile globale
numero = 10

def funzione_esterna():

    # Variabile locale nella funzione esterna
    numero = 5
    print("Numero dentro funzione_esterna (Locale):", numero)

    def funzione_interna():

        # Utilizzo nonlocal per modificare la variabile locale della funzione esterna
        nonlocal numero
        numero = 3
        print("Numero dentro funzione_interna (nonlocal):", numero)

    funzione_interna()

print("Numero nel main (globale):", numero)
funzione_esterna()
print("Numero nel main dopo chiamata (globale non cambiato):", numero)


#in python non esistono le ke



# Le variabili o metodi privati sono definiti con due trattini bassi (__)
# Questo attiva il name mangling

class MiaClasse:
    def __init__(self):
        self.__variabile_privata = "Sono privata"

    def __metodo_privato(self):
        return "Questo è un metodo privato"


obj = MiaClasse()

# Stampando direttamente la variabile privata solleverà un'eccezione
# print(obj.__variabile_privata)  # AttributeError

# L'accesso corretto (che dovrebbe essere evitato) sarebbe:
print(obj._MiaClasse__variabile_privata)  # Funzionerà, ma non è buona prassi


#PROTETTI:
# Le variabili o metodi protetti si indicano con un singolo trattino basso (_)
# Non esiste un meccanismo tecnico che impedisce l’accesso dall’esterno.

class ClasseBase:
    def __init__(self):
        self._variabile_protetta = "Sono protetta"


class SottoClasse(ClasseBase):
    def __init__(self):
        super().__init__()
        print(self._variabile_protetta)  # Accesso consentito


obj = SottoClasse()

# Accesso da fuori la classe (non consigliato, ma possibile)
print(obj._variabile_protetta)


