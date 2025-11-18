class MembroSquadra:
    def __init__(self,nome,età):
        self.nome = nome
        self.età = età
        
    def descrivi(self):
        print(f" {self.nome}, {self.età} anni , è un membro della squadra ")
        
class Giocatore(MembroSquadra):
    def __init__(self,nome, età , ruolo, numero_maglia):
        super().__init__(nome, età)
        self.ruolo = ruolo
        self.numero_maglia = numero_maglia
        
    def gioca_partita(self):
        super().descrivi()
        print(f"{self.nome}, {self.età} con il numero {self.numero_maglia} di ruolo {self.ruolo} gioca titolare!")
        
class Allenatore(MembroSquadra):
    def __init__(self,nome, età, anni_di_esperienza):
        super().__init__(nome, età)
        self.anni_di_esperienza = anni_di_esperienza
    
    def dirige_allenamento(self):
        super().descrivi()
        print(f"L'allenatore {self.nome} {self.età} con {self.anni_di_esperienza} anni di esperienza , dirige l'allenamento al centro sportivo")
        
class Assistente(MembroSquadra):
    def __init__(self, nome, età,specializzazione):
        super().__init__(nome, età)
        self.specializzazione = specializzazione