# Import delle varie classi dal file esercizio_teatro
from esercizio_teatro import Teatro, Posto, PostoVip, PostoStandard

# Creiamo un oggetto Teatro
teatro = Teatro()

# Creiamo tre posti diversi
posto1 = Posto(1, "D")                     # un posto generico numero 1, fila D
posto2 = PostoStandard(5, "C", 20)         # posto standard numero 5, fila C, costo 20
posto3 = PostoVip(4, "A", "servizi extra inclusi")  # posto VIP numero 4, fila A, con servizi extra

# Aggiungiamo i posti al teatro
teatro.aggiungi_posto(posto1)
teatro.aggiungi_posto(posto2)
teatro.aggiungi_posto(posto3)

# Prenotiamo i posti
teatro.prenota_posto(1, "D")               # prenota il posto generico 1D
teatro.prenota_posto(5, "C")               # prenota il posto standard 5C
teatro.prenota_posto(20, "G")              # prova a prenotare un posto inesistente, stampa "Posto non trovato."


