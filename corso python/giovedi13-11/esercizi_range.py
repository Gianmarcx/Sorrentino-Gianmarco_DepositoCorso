ripeti = "si" 

while ripeti == "si":
    scelta = input("Vuoi inserire un numero o una stringa? (n/s): ") #chiede se si vuole dare come input un numero o una stringa
    
    #se la scelta è un numero chiede di inserire un numero per poi effettuare la verifica
    if scelta == "n":
        numero = int(input("Inserisci un numero: "))
        if numero % 2 == 0: #controlla se è pari o dispari
            print(f"Il numero {numero} è pari")
        else:
            print(f"Il numero {numero} è dispari")
            
    elif scelta == "s":
        stringa = input("Inserisci una stringa: ") 
        print(f"Hai scritto: {stringa}") #ripete la stringa che da noi scritta

    else:
        print("Scelta non riconosciuta")
    
    ripeti = input("Vuoi ripetere? (si/no): ")

print("STOP")


#Esercizio 2

ripeti = "si" 

while ripeti == "si":
    numero_iniziale = int(input("Inserisci primo numero dell'intervallo: "))
    numero_finale = int(input("Inserisci numero finale dell'intervallo:"))
    
    numeri_primi = []
    numeri_non_primi = []
    
