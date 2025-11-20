#crediti a Giuseppe D'avanzo

import random
class Elettrodomestico:
    def __init__(self,marca,modello,anno_acquisto,guasto):
        self.__marca = marca
        self.__modello = modello
        self.__anno_acquisto = anno_acquisto
        self.__guasto = guasto
        
    def get__marca(self):
        return self.__marca
    
    def set__marca(self,marca):
        self.__marca = marca 
    
    def get__modello(self):
        return self.__modello
    
    def set__marca(self,modello):
        self.__modello = modello
        
    def get__anno_acquisto(self):
        return self.__anno_acquisto
    
    def set__anno_acquisto(self,anno_acquisto):
        self.__anno_acquisto = anno_acquisto
        if self.__anno_acquisto > 2025:
            print("Anno acquisto sbagliato!!!")
    
    def get__guasto(self):
        return self.__guasto
    
    def set__guasto(self,guasto):
         self.__guasto = guasto
         
    def descrizione(self):
        print(f"Marca: {self.__marca} Modello: {self.__modello} Anno Acquisto: {self.__anno_acquisto} Guasto: {self.__guasto} ")
        
    def stima_costo_base(self):
        return random.randint(150,1000)
    
class Lavatrice(Elettrodomestico):
    def __init__(self, marca, modello, anno_acquisto, guasto,capacita_kg,giri_centrifuga):
        super().__init__(marca, modello, anno_acquisto, guasto)
        self.capacita_kg = capacita_kg
        self.giri_centrifuga = giri_centrifuga
        
    def stima_costo_base(self):
        if self.capacita_kg > 3:
            return random.randint(200,300)
        
class Frigorifero(Elettrodomestico):
    def __init__(self, marca, modello, anno_acquisto, guasto,litri,ha_freezer):
        super().__init__(marca, modello, anno_acquisto, guasto)
        self.litri = litri
        self.ha_freezer = ha_freezer
        
    def stima_costo_base(self):
        if self.litri > 300:
          return random.randint(300,400)
      
class Forno(Elettrodomestico):
    def __init__(self, marca, modello, anno, guasto, tipo_alimentazione, ha_ventilato):
        super().__init__(marca, modello, anno, guasto)
        self.tipo_alimentazione = tipo_alimentazione
        self.ha_ventilato = ha_ventilato

    def stima_costo_base(self):
        base = random.randint(70, 120)
        if self.tipo_alimentazione == "gas":
            base += 20
        if self.ha_ventilato:
            base += 30
        return base
    
    
class TicketRiparazione:
    def __init__(self,id_ticket,elettrodomestico):
        self.__id_ticket = id_ticket 
        self.__elettrodomestico = elettrodomestico
        self.__stato = True
        self.__note = []
        
    def get_id_ticket(self):
        return self.__id_ticket

    def get_elettrodomestico(self):
        return self.__elettrodomestico

    def get_stato(self):
        return self.__stato

    def set_stato(self, stato):
        if stato not in ["aperto", "in lavorazione", "chiuso"]:
            raise ValueError("Stato non valido")
        self.__stato = stato

    def aggiungi_nota(self,testo):
        testo = input("Inserisci stringa: ")
        testo.append(self.__note)
        
    def calcola_preventivo(self, *voci_extra):
        costo_base = super().stima_costo_base()
        totale = costo_base + sum(voci_extra)
        descrizione = (f"Costo base:{costo_base} | Voci Extra: {voci_extra} | Totale : {totale} ")
        return descrizione 
        
    def stampa_note(self):
        return "\n".join(self.__note) if self.__note else "Nessuna nota"
    def descrizione_ticket(self):
        
        return f"Ticket {self.__id_ticket} - Stato: {self.__stato} - Elettrodomestico: {type(self.__elettrodomestico).__name__}"
    
class Officina:
    def __init__(self,nome,tickets):
        
    
        
        
            
        
    
    
        


    