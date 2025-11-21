from abc import ABC, abstractmethod

class VeicoloTrasporto(ABC):
    def __init__(self,targa,peso_massimo):
            self._targa = targa
            self._peso_massimo = peso_massimo
            self._carico_attuale = 0
            
    def carica(self, peso):
        if self._carico_attuale + peso <= self._peso_massimo:
            self._carico_attuale += peso
            print(f"Caricati {peso} kg. Carico attuale: {self._carico_attuale} kg.")
        else:
            print("Errore: carico eccede la capacità massima!")
        
    def scarica(self):
        print(f"Scaricati {self._carico_attuale} kg.")
        self._carico_attuale = 0

        
    @abstractmethod
    def costo_manutenzione(self):
        pass
        
class Camion(VeicoloTrasporto):
    def __init__(self, targa, peso_massimo,numero_assi):
        super().__init__(targa, peso_massimo)                
        self.numero_assi = numero_assi
        
    def costo_manutenzione(self):
        return 100 * self.numero_assi + 1 * self._peso_massimo
    
class Furgone(VeicoloTrasporto):
    def __init__(self, targa, peso_massimo,alimentazione):
         super().__init__(targa, peso_massimo)
         self.alimentazione = alimentazione
         
    def costo_manutenzione(self):
        if self.alimentazione == "Elettrico":
            return 200
        if self.alimentazione == "Diesel":
            return 150
        else:
            return 0
        
        
class MotoCarro(VeicoloTrasporto):
    def __init__(self, targa, peso_massimo,anni_servizio):
         super().__init__(targa, peso_massimo)
         self.anni_servizio = anni_servizio
         
    def costo_manutenzione(self):
        return 50 * self.anni_servizio
        
class GestoreFlotta:
    def __init__(self):
        self.veicoli = []
        
    def aggiungi_veicolo(self,veicolo):
        self.veicoli.append(veicolo)
    
    def rimuovi_veicolo(self,targa):
        self.veicoli = [veicolo for veicolo in self.veicoli if veicolo._targa != targa]
        
    def costo_totale_manutenzione(self):
        return sum(veicolo.costo_manutenzione() for veicolo in self.veicoli)

    def stampa_veicoli(self):
        for veicolo in self.veicoli:
            print(f"Targa: {veicolo._targa}, Tipo: {type(veicolo).__name__}, Carico attuale: {veicolo._carico_attuale} kg")