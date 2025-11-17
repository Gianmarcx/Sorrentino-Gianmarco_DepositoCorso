class Ristorante:
    def __init__(self, nome, tipo_di_cucina):
        self.nome = nome
        self.tipo_di_cucina = tipo_di_cucina
        self.aperto = False
        self.menu = {}
        
    def imposta_stato_input(self):
        scelta = input("Vuoi che il ristorante sia aperto o chiuso? ").strip().lower()
        if scelta == "aperto":
            self.aperto = True
        elif scelta == "chiuso":
            self.aperto = False
        print(f"Il Ristorante '{self.nome}'è '{scelta}'")
        
    def descrivi_ristorante(self):
        print(f"Il Ristorante '{self.nome}' offre cucina '{self.tipo_di_cucina}'")
            
            
    def aggiungi_al_menu(self):
        piatto = input("Inserisci il nome del piatto da aggiungere").strip()
        self.menu[piatto] = piatto
        print(f"Il piatto '{piatto}' aggiunto al menu")
            
    def togli_dal_menu(self):
        piatto = input("Inserisci il nome del piatto da rimuovere: ").strip()
        if piatto in self.menu:
            del self.menu[piatto]
            print(f"Il piatto '{piatto}' è stato rimosso")
        else:
            print("Piatto non presente nel menu")
                
    def stampa_menu(self):
        print(self.menu)

        
mio_ristorante = Ristorante("Il pescatore","di mare")
mio_ristorante.descrivi_ristorante()
mio_ristorante.imposta_stato_input()
mio_ristorante.aggiungi_al_menu()
mio_ristorante.stampa_menu()
mio_ristorante.togli_dal_menu()
mio_ristorante.stampa_menu()