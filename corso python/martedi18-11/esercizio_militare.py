class UnitaMilitare:
    def __init__(self,nome,numero_soldati):
        self.nome = nome
        self.numero_soldati = numero_soldati
        
    def muovi(self):
        print(f"L'unita militare {self.nome} composta da {self.numero_soldati} soldati, si muove verso nord ")
        
    def attacca(self):
        print(f"L'unita militare {self.nome} attacca nord con {self.numero_soldati} soldati")
        
    def ritira(self):
        print(f"L'unita militare {self.nome} composta da {self.numero_soldati} soldati, si ritira alla base")
        
class Fanteria(UnitaMilitare):
    def __init__(self,nome,numero_soldati):
        super().__init__(nome,numero_soldati)
        self.nome = nome
        self.numero_soldati = numero_soldati
    
    def costruisci_trincea(self):
        super().muovi()
        print(f"La fanteria dell'unità militare {self.nome} composta da {self.numero_soldati} costruisce una trincea")
        
class Artiglieria(UnitaMilitare):
    def __init__(self,nome,numero_soldati):
        super().__init__(nome,numero_soldati)
        self.nome = nome
        self.numero_soldati = numero_soldati
        
    def calibra_artiglieria(self):
        super().muovi()
        print(f"l'unità militare {self.nome} composta da {self.numero_soldati} soldati, calibra l'artiglieria")
        
class Cavalleria(UnitaMilitare):
    def __init__(self,nome,numero_soldati):
        super().__init__(nome,numero_soldati)
        self.nome = nome
        self.numero_soldati = numero_soldati
        
    def esplora_terreno(self):
        print(f"La cavalleria appartentente dell'unità militare {self.nome} composta da {self.numero_soldati} soldati, esplora l'area per raccogliere informazioni ")
        
class SupportoLogistico(UnitaMilitare):
    def __init__(self,nome,numero_soldati):
        super().__init__(nome,numero_soldati)
        self.nome = nome
        self.numero_soldati = numero_soldati
    
    def rifornisci_unita(self):
        print(f"Il supporto logistico gestisce rifornimento e manutenzione per l'unità militare {self.nome} composta da {self.numero_soldati} soldato")
            
class Ricognizione(UnitaMilitare):
    def __init__(self,nome,numero_soldati):
        super().__init__(nome,numero_soldati)
        self.nome = nome
        self.numero_soldati = numero_soldati
        
    def conduci_ricognizione(self):
        print(f"L'unità di ricognizione appartenente all'unita militare {self.nome} composta da {self.numero_soldati} soldati conduce missioni di sorveglianza")
        
        
class ControlloMilitare(UnitaMilitare,Fanteria,Artiglieria,Cavalleria,SupportoLogistico,Ricognizione):
    def __init__(self):
        self.unita_registrate = {}
        
    def registra_unita(self,unita):
        self.unita_registrate[unita.nome] = unita
        print(f"Unità {unita.nome} registrata")
        
    def mostra_unita(self):
        print("unità registrate: ")
        for nome in self.unita_registrate:
            print(f"-{nome}")
            
    def dettagli_unita(self, nome_unita):
        if nome_unita in self.unita_registrate:
            unita = self.unita_registrate[nome_unita]
            print(f"Dettagli {nome_unita}: {unita.numero_soldati} soldati, Tipo: {type(unita).__name__}")
        else:
            print(f"Unità {nome_unita} non trovata.")
            

            
        
        
        
        