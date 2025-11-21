from dipendente import Dipendente


class Turni(Dipendente):
    tipi_di_turni = ["MATTINA" , "POMERIGGIO" , "NOTTE"]
     
    def __init__(self, nome, eta, ruolo, badge,tipo_turno):
        super().__init__(nome, eta, ruolo, badge)
        self.tipo_turno = tipo_turno
        
      
        
    def descrizione_turno(self,tipi_di_turni):
        if self.tipo_turno not in tipi_di_turni:
            raise ValueError("Turno non valido")
        print(f"Il dipendente {self.get__nome()} di anni {self.get__eta()} che ricopre il ruolo {self.get__ruolo()}, che possiede il badge {self.get__badge()}, ha il turno di {self.tipo_turno}")