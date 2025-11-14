#il match consente di confrontare il valore di una variabile con diversi pattern, eseguendo un blocco di codice specifico quando trova una corrispondenza

comando =input("Inserisci un comando:")

match comando:
    case "start":
        print("Avvio del programma.")
    case "stop":
        print("Chiusura del programma.")
    case "pausa":
        print("Programma in pausa.")
    case _:
        print("comando non riconosciuto")