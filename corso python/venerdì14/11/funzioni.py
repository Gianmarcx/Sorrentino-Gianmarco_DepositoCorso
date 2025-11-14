#le funzioni sono blocchi di codice autonomi che eseguono una determinata operazione.
#le funzioni sono la più grande prova pratica che l'astrazione esiste 
#le funzioni consentono di organizzare il codice in unità modulari e aiutano a scrivere il codice più leggibile e compresibile

#le definiamo attraverso def seguita dal nome della funzione e da una coppia di () e con : per terminare


def saluta(nome):
    print("Ciao,",nome)
    
#per eseguire il blocco di codice di una funzione devi chiamarla
#i parametri sono variabili che consentono di passare dati alla funzioni,si specificano tra parentesi () nella definizione della funzione
#si possono definire "n" parametri e assegnare loro nomi significativi

saluta("Alice")
somma(5,3)

def somma(a,b):
    risultato = a + b
    print("La somma è", risultato) 
    
#esistono due tipi di funzioni: quelle con il return nullo(None) e 

