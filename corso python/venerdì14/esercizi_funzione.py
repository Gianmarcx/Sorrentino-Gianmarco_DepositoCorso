import random

# Funzione per generare un numero casuale tra 1 e 100
def genera_numero():
    return random.randint(1, 100)

# Funzione per chiedere all'utente di inserire un numero
def chiedi_risposta():
    return int(input("Inserisci un numero: "))

# Funzione principale del gioco
def gioco():
    numero_casuale = genera_numero()
    tentativi = 0

    print("Prova ad indovinare il numero casuale da 1 a 100:")

    while True:
        numero_utente = chiedi_risposta()
        tentativi += 1

        if numero_utente < numero_casuale:
            print("Il numero è troppo basso, riprova:")
        elif numero_utente > numero_casuale:
            print("Il numero è troppo grande, riprova:")
        else:
            print(f"Hai indovinato il numero {numero_casuale} in {tentativi} tentativi! Congratulazioni!!!")
            break

# Avvia il gioco
gioco()

    
