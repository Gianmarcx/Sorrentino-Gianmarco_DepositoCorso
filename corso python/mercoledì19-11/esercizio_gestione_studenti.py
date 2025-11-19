# Classe base Persona: rappresenta una persona generica
class Persona:
    # Costruttore: inizializza nome e età come attributi privati
    def __init__(self,nome,eta):
        self.__nome = nome
        self.__eta = eta
        
    # Setter per il nome (modifica il nome)
    def set_nome(self, nome):
        self.__nome = nome 
        
    # Getter per il nome (restituisce il nome)
    def get_nome(self):
        return self.__nome
    
    # Setter per l'età (modifica l'età)
    def set_eta(self, eta):
        self.__eta = eta
        
    # Getter per l'età (restituisce l'età)
    def get_eta(self):
        return self.__eta
    
    # Metodo generico di presentazione della persona
    def presentazione(self):
        print(f"Ciao sono {self.__nome} e ho {self.__eta} anni! ")

# Sottoclasse Studente che eredita da Persona
class Studente(Persona):
    # Costruttore: inizializza nome, età e voti dello studente
    def __init__(self, nome, eta, voti):
        super().__init__(nome,eta)  # Chiama il costruttore della classe base Persona
        self.__voti = []  # Lista privata dei voti
        
        # Chiede all'utente di inserire i voti separati da spazi
        voti = input("Inserire voti: ")
        # Trasforma i voti in interi e li aggiunge alla lista dei voti
        self.__voti.extend([int(voto) for voto in voti.split()])
        
    # Metodo per calcolare la media dei voti
    def calcola_media(self):
        totale = 0
        for voto in self.__voti:
            totale += voto  # Somma tutti i voti
        if len(self.__voti) == 0:
            return 0  # Se non ci sono voti, restituisce 0
        return totale/len(self.__voti)  # Restituisce la media
    
    # Override del metodo presentazione (polimorfismo)
    def presentazione(self):
        media = self.calcola_media()  # Calcola la media dei voti
        # Stampa la presentazione dello studente includendo la media
        print(f"Salve sono {self.get_nome()} ho {self.get_eta()} anni, e ho una media voto pari a {media}")

# Sottoclasse Professore che eredita da Persona
class Professore(Persona):
    # Costruttore: inizializza nome, età e materia insegnata
    def __init__(self, nome, eta, materia):
        super().__init__(nome,eta)  # Chiama il costruttore della classe base Persona
        # Chiede all'utente di inserire la materia insegnata
        self.materia = input("Inserisci materia: ")
        
    # Override del metodo presentazione (polimorfismo)
    def presentazione(self):
        # Stampa la presentazione del professore includendo la materia
        print(f"Salve sono {self.get_nome()} ho {self.get_eta()} anni, e insegno {self.materia}")
