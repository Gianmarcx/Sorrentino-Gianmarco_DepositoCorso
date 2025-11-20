from abc import ABC, abstractmethod

# Classe astratta base: contiene attributi comuni e il metodo astratto
class Impiegato(ABC):
    def __init__(self,nome,cognome,stipendio_base):
        self.nome = nome                  # nome dell'impiegato
        self.cognome = cognome            # cognome dell'impiegato
        self.stipendio_base = stipendio_base  # stipendio base

    @abstractmethod
    def calcola_stipendio(self):
        pass  # metodo da implementare nelle sottoclassi


# Impiegato con stipendio fisso: restituisce solo lo stipendio base
class ImpiegatoFisso(Impiegato):
    def calcola_stipendio(self):
        return self.stipendio_base       # restituisce lo stipendio base


# Impiegato a provvigione: stipendio base + bonus sulle vendite
class ImpiegatoAProvvigione(Impiegato):
    def __init__(self, nome, cognome, stipendio_base, vendite, percentuale_bonus):
        super().__init__(nome, cognome, stipendio_base)  # inizializza campi comuni
        self.vendite = vendite            # totale vendite (es. in euro)
        self.percentuale_bonus = percentuale_bonus  # es. 0.10 per 10%

    def calcola_stipendio(self):
        bonus_per_stipendio = self.vendite * self.percentuale_bonus
                                         # calcola il bonus = vendite * percentuale
        return self.stipendio_base + bonus_per_stipendio
                                         # restituisce stipendio totale

    def informazioni(self):
        stipendio_totale = self.calcola_stipendio()  # ottiene il valore calcolato
        print(f"Nome: {self.nome}, Cognome: {self.cognome}, Stipendio Totale: {stipendio_totale}")
                                         # stampa le informazioni in modo leggibile


# Esempio d'uso:
imp = ImpiegatoAProvvigione("Gianmarco", "Sorrentino", 1000, 5000, 0.10)
imp.informazioni()  # chiamata che stampa: Nome..., Cognome..., Stipendio Totale: 1500.0
