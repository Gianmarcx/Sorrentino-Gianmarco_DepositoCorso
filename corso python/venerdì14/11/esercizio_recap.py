lista_ordini = [] #lista vuota che conterrà gli ordini effettuati


def crea_ordine(deposito): #funzione crea ordine che chiede che genere alimentare si cerca
    genere_alimentare = input("Che genere alimentare cerchi? (Pasta, Carne, Frutta): ")

    # crea una lista con tutti gli elementi del deposito che hanno quel genere
    #deposito è una lista di tuple
    generi_trovati = [item for item in deposito if item[0] == genere_alimentare]

    #se il genere non è disponibile stampa "Genere non disponibile"
    if not generi_trovati:
        print("Genere non disponibile")
        return
    
    #variabile alimento che chiede di dare in input che genere alimentare si vuole
    alimento = input(f"Scrivi alimento nel genere alimentare {genere_alimentare}:")

    #Ciclo for su tutti gli elementi presenti nel deposito , utilizzando gli indici
    for i in range(len(deposito)): #range(len(deposito)) permette di modificare 
        genere, nome, quantità_disponibile = deposito[i]  
        
        #controlla se l'elemento corrisponde a quello cercato   
        if genere == genere_alimentare and nome == alimento:
            
            #chiede di inserire in input la quantità richiesta
            quantità_richiesta = int(input("Inserisci quantità: "))
            
            #controlla se la quantità richiesta è disponibile
            if quantità_richiesta > quantità_disponibile:
                print("Quantità non disponibile")
                return #il return ci fa uscire poichè non è possibile completare l'ordine

            # Aggiorno la quantità ma visto che le tuple sono immutabile bisogna crearne una nuova
            deposito[i] = (genere, nome, quantità_disponibile - quantità_richiesta)

            #aggiunge l'ordine alla lista ordini
            lista_ordini.append((genere_alimentare, alimento, quantità_richiesta))
            
            #stampa i dettagli dell'ordine appena effettuato
            print(f"Ordine per {quantità_richiesta} {alimento} aggiunto!\n")
            return #esce falla funzione poichè l'ordine è completo

    print("Alimento non trovato")


def visualizza_ordini():
    if not lista_ordini: #avviso se la lista ordini è vuota
        print("Nessun ordine trovato\n")
    else:
        print("Ecco la cronologia degli ordini:") 
        for genere, alimento, quantità_richiesta in lista_ordini: #altrimenti stampa la lista degli ordini effettuati 
            print(f"Genere: {genere}, Alimento: {alimento}, Quantità: {quantità_richiesta}")
        


def menu_ordini(deposito): #menu che resta in loop fin quando non si sceglie un opzione
    while True:
        print("Scegli un'opzione:")
        print("1. Crea nuovo ordine")
        print("2. Cronologia ordini")
        print("3. Torna al menu principale")

        scelta = int(input("Quale opzione hai scelto: ")) #variabile scelta che chiede di dare in input una delle opzioni presenti nel meni

        if scelta == 1: #opzione 1 chiama la funzione per creare un ordine
            crea_ordine(deposito)
        elif scelta == 2: #opzione 2 chiama la funzione per visualizzare cronologia ordini
            visualizza_ordini()
        elif scelta == 3: #torna al menù principale
            print("Torno al menu principale")
            break #interrompe il ciclo
        else:
            print("Opzione non valida") #stampa se si sceglie un opzione non presente nel menù

                     
                
                    
                
            
            
    
        
        
        