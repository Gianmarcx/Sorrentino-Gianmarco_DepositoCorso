# Classe base che rappresenta un posto generico
class Posto:
    def __init__(self, numero, fila):
        self._numero = numero          # numero del posto
        self._fila = fila              # fila del posto
        self._occupato = False         # stato iniziale: il posto non è occupato
        
    # Metodo per prenotare il posto
    def prenota(self):
        if not self._occupato:         # se il posto non è già occupato
            self._occupato = True      # lo prenota
            print("Posto Prenotato!")
        else:                          # altrimenti dice che è già occupato
            print("Posto già Occupato")

    # Metodo per liberare il posto
    def libera(self):
        if self._occupato:             # se il posto è occupato
            self._occupato = False     # lo libera
            print("Posto liberato!")
        else:                          # altrimenti
            print("Il posto era già libero")

    # Getter per ottenere il numero del posto
    def get_numero(self):
        return self._numero
    
    # Getter per ottenere la fila del posto
    def get_fila(self):
        return self._fila
    
    # Getter per verificare se il posto è occupato
    def get_occupato(self):
        return self._occupato


# Sottoclasse  PostoVip, eredita attributi classe base Posto aggiungendo attributo servizi_extra
class PostoVip(Posto):
    def __init__(self, numero, fila, servizi_extra):
        super().__init__(numero, fila) # chiama il costruttore della classe base
        self.servizi_extra = servizi_extra  # servizi aggiuntivi del posto VIP
        
    # Override del metodo prenota per aggiungere info sui servizi VIP
    def prenota(self):
        if not self._occupato:
            self._occupato = True
            print(f"Posto Vip prenotato con seguenti servizi extra {self.servizi_extra} ")
        else:
            print("Posto già occupato")


# Sottoclasse per posti standard, eredita attributi e aggiung attributo costo
class PostoStandard(Posto):
    def __init__(self, numero, fila, costo):
        super().__init__(numero, fila) # chiama il costruttore della classe base
        self.costo = costo              # costo del posto standard
        
    # Override del metodo prenota per mostrare il costo
    def prenota(self):
        if not self._occupato:
            self._occupato = True
            print(f"Posto Standard numero {self._numero} della fila {self._fila} prenotato al costo di {self.costo}")
        else:
            print("Posto già occupato")


# Classe che rappresenta il teatro e gestisce tutti i posti
class Teatro:
    def __init__(self):
        self._posti = []   # lista di tutti i posti presenti nel teatro

    # Metodo per aggiungere un posto alla lista
    def aggiungi_posto(self, posto):
        self._posti.append(posto)

    # Metodo per prenotare un posto specifico tramite numero e fila
    def prenota_posto(self, numero, fila):
        for posto in self._posti:                        # scorre tutti i posti
            if posto.get_numero() == numero and posto.get_fila() == fila:  # trova corrispondenza
                posto.prenota()                           # chiama il metodo prenota del posto
                return
        print("Posto non trovato.")                      # se non trova il posto, stampa messaggio

    # Metodo per stampare tutti i posti occupati
    def stampa_posti_occupati(self):
        print("Ecco i posti occupati:")
        for posto in self._posti:
            if posto.get_occupato():                      # controlla solo i posti occupati
                print(f"Fila {posto.get_fila()}, Numero {posto.get_numero()}")
