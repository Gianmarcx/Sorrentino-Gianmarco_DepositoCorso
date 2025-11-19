# Importa la classe Persona dal modulo esercizio_gestione_studenti
from esercizio_gestione_studenti import Persona,Studente,Professore

# Funzione principale del programma
def main():
    lista_persone = []  # Lista vuota che conterrà tutti gli studenti e professori creati

    # Ciclo infinito per mostrare il menù finché l'utente non sceglie di uscire
    while True:
        print("\n--- Menù ---")
        print("1. Crea Studente")
        print("2. Crea Professore")
        print("3. Mostra tutte le presentazioni")
        print("4. Esci")

        scelta = input("Scegli un'opzione: ")  # L'utente inserisce la scelta

        # Se l'utente sceglie 1 → creare uno studente
        if scelta == "1":
            nome = input("Nome studente: ")          # Chiede il nome
            eta = int(input("Età studente: "))       # Chiede l'età
            studente = Studente(nome, eta, None)     # Crea l'oggetto Studente; i voti vengono richiesti dentro il costruttore
            lista_persone.append(studente)           # Aggiunge lo studente alla lista

        # Se l'utente sceglie 2 → creare un professore
        elif scelta == "2":
            nome = input("Nome professore: ")        # Chiede il nome
            eta = int(input("Età professore: "))     # Chiede l'età
            professore = Professore(nome, eta, None) # Crea l'oggetto Professore; la materia viene richiesta dentro il costruttore
            lista_persone.append(professore)        # Aggiunge il professore alla lista

        # Se l'utente sceglie 3 → mostra tutte le presentazioni
        elif scelta == "3":
            for p in lista_persone:                 # Per ogni persona nella lista
                p.presentazione()                   # Chiama il metodo presentazione (polimorfico)

        # Se l'utente sceglie 4 → esce dal programma
        elif scelta == "4":
            print("Uscita dal programma.")
            break  # Esce dal ciclo while

        # Gestione scelta non valida
        else:
            print("Scelta non valida!")

# Punto di ingresso del programma
if __name__ == "__main__":
    main()  # Chiama la funzione main
