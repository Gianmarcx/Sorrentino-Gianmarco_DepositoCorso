class Prodotto:
    
    def __init__(self):
        def __init__(self, nome, costo_produzione, prezzo_vendita):
            self.nome = nome
            self.costo_produzione = costo_produzione
            self.prezzo_vendita = prezzo_vendita
            
    def calcola_profitto(self):
        return self.prezzo_vendita - self.costo_produzione 
    
    
class Abbigliamento:
    def __init__(self, nome, costo_produzione, prezzo_vendita, materiale):
        self.nome = nome
        self.costo_produzione = costo_produzione
        self.prezzo_vendita = prezzo_vendita
        self.materiale = materiale

    def calcola_profitto(self):
        return self.prezzo_vendita - self.costo_produzione


class Elettronica:
    def __init__(self, nome, costo_produzione, prezzo_vendita, garanzia_anni):
        self.nome = nome
        self.costo_produzione = costo_produzione
        self.prezzo_vendita = prezzo_vendita
        self.garanzia_anni = garanzia_anni

    def calcola_profitto(self):
        return self.prezzo_vendita - self.costo_produzione

        
    


