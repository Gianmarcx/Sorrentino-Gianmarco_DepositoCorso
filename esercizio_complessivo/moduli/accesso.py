from dipendente import Dipendente
from turni import Turni

class Accesso:
    def __init__(self):
        self.log = []
        
    def tipo_di_log(self,dipendente,log):
        registra = (f"NOME : {dipendente.get__nome()} ETA: {dipendente.get__eta()} RUOLO: {dipendente.get__ruolo()} , BADGE: {dipendente.get__badge()}")
        
        if hasattr(dipendente, "tipo_turno"):
            registra += print(f" TURNO: {dipendente.tipi_turno}")
            
        registra += print(f"{log}")
        self.log.append(registra)
        print(registra)
        
    def mostra_log(self):
        print("===LOG===")
        for registra in self.log:
            return registra