# Classe base che definisce l'interfaccia/metodo generico per i pagamenti
class MetodoPagamento:
    def effettua_pagamento(self, importo):
        self.importo = importo  # salva l'importo da pagare


# Sottoclasse che simula un pagamento con carta di credito
class CartaDiCredito(MetodoPagamento):
    def effettua_pagamento(self, importo):
        super().effettua_pagamento(importo)  
        # richiama il metodo della classe base per memorizzare l'importo
        print(f"Pagamento di importo {self.importo} effettuato con Carta di Credito!")
        # stampa un messaggio specifico


# Sottoclasse che simula un pagamento tramite PayPal
class PayPal(MetodoPagamento):
    def effettua_pagamento(self, importo):
        super().effettua_pagamento(importo)  
        # richiama il metodo della classe base
        print(f"Pagamento di importo {self.importo} effettuato con PayPal!")
        # stampa un messaggio specifico


# Sottoclasse che simula un pagamento tramite bonifico bancario
class BonificoBancario(MetodoPagamento):
    def effettua_pagamento(self, importo):
        super().effettua_pagamento(importo)  
        # richiama il metodo della classe base
        print(f"Pagamento di importo {self.importo} effettuato tramite BonificoBancario!")
        # stampa un messaggio specifico


# Gestore che utilizza un metodo di pagamento senza preoccuparsi del tipo
class GestorePagamenti:
    def __init__(self, metodo):
        self.metodo = metodo  # salva l'oggetto di pagamento passato

    def effettua_pagamento(self, importo):
        # chiama il metodo effettua_pagamento dell'oggetto salvato
        # non importa se è Carta, PayPal o Bonifico
        self.metodo.effettua_pagamento(importo)
