class Veicolo:
    def __init__(self,marca,modello,anno,accensione):
        self._marca = marca
        self._modello = modello
        self._anno = anno
        self._accensione = accensione
        
    def get_marca(self):
        return self._marca
    
    def get_modello(self):
        return self._modello
    
    def get_anno(self):
        return self._anno
    
    def accendi(self):
        self._accensione = True
        print(f"{self._marca}, {self._modello} è acceso ")
        
    def spegni(self):
        self._accensione = False
        print(f"{self._marca} {self._modello} è spento ")
        
class Auto(Veicolo):
    def __init__(self,marca,modello,anno,accensione,numero_porte):
        super().__init__(marca,modello,anno,accensione)
        self._numero_porte = numero_porte
            
    def suona_clacson(self):
        print(f"{self._marca}{self._modello} suona il clacson! ")
        
class Furgone(Veicolo):
    def __init__(self,marca,modello,anno,accensione,capacita_carico):
        super().__init__(marca,modello,anno,accensione)
        self._capacita_carico = capacita_carico
        
    def carica(self):
        print(f"{self._marca} {self._modello} carica la merce!")
        
    def scarica(self):
         print(f"{self._marca} {self._modello} scarica la merce!")

class Motocicletta(Veicolo):
    def __init__(self,marca,modello,anno,accensione,tipo):
        super().__init__(marca,modello,anno,accensione)
        self._tipo = tipo

    def esegui_wheelie(self):
        if self._tipo == "sportivo":
            print(f"{self._marca}{self._modello} esegue un wheelie!")
        else:
            print(f"{self._marca}{self._modello} non esegue un wheelie perchè non è sportiva")
            
class GestoreParcoVeicoli:
    def __init__(self):
        self._veicoli = []
    
    def aggiungi_veicolo(self,veicolo):
        self._veicoli.append(veicolo)
        print(f"{veicolo.get_marca()} {veicolo.get_modello()} aggiunto al parco.")
                 
    def rimuovi_veicolo(self,veicolo,marca,modello):
        for veicolo in self._veicoli:
            if veicolo.get_marca() == marca and veicolo.get_modello() == modello:
                self._veicoli.remove(veicolo)
                print("Rimosso!")
                return
            print("Veicolo non trovato")
            
    def lista_veicoli(self):
        return self._veicoli

    def menu():
    
# Creiamo alcune Auto
auto1 = Auto("Fiat", "Panda", 2020, 5, "benzina" )
auto2 = Auto("Tesla", "Model 3", 2022, 4, "elettrica")

# Creiamo alcuni Furgoni
furgone1 = Furgone("Ford", "Transit", 1200)
furgone2 = Furgone("Mercedes", "Sprinter" 1500)

# Creiamo alcune Motociclette
moto1 = Motocicletta("Yamaha", "MT-07", "sportiva")
moto2 = Motocicletta("Ducati", "Panigale V4", "sportiva")
        
while True:
            print("===MENU VEICOLI===")
            print("1.Aggiugi Auto")
            print("2.Aggiungi Furgone")
            print("3.Aggiugi Motocicletta")
            print("4.Accendi Veicolo")
            print("5.Spegni Veicolo")
            print("6.Mosta lista veicoli")
            print("7.Esci")

            scelta = input("Scegli Opzione")
            

            if scelta == "1":
            # aggiungi_veicolo()
            pass

            elif scelta == "2":
            # rimuovi_veicolo()
            pass

            elif scelta == "3":
            # lista_veicoli()
            pass

            elif scelta == "4":
            # accendi_veicolo()
            pass

            elif scelta == "5":
            # spegni_veicolo()
            pass

            elif scelta == "0":
                print("Chiusura programma...")
            break

            else:
                print("Scelta non valida.")
       
    
                
            
        
    