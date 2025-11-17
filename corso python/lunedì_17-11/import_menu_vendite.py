from analizzatori_dati_vendita import inserisci_importi #importa la funzione per l'inserimento degli importi di vendita


def menu_vendite():
    importi_vendita = []  # Lista iniziale vuota che conterrà tutti gli importi inseriti

    while True: #ciclo while del menu che mostra le opzioni fin quando non ne viene scelta una 
        print("\n--- Menu Vendite ---")
        print("1. Inserisci nuove vendite")
        print("2. Mostra totale e media delle vendite")
        print("3. Esci")

       
        scelta = int(input("Quale opzione hai scelto: ")) #chiede in input un delle opzioni presenti nel menù
        

        if scelta == 1:
            # Richiamo della funzione di inserimento
            nuovi_importi = inserisci_importi()
            importi_vendita.extend(nuovi_importi) #aggiunge i nuovi importi alla lista princiapale
            print("Vendite aggiornate:", importi_vendita)

        elif scelta == 2:
            if importi_vendita: #mostra totale e media degli importi , solo se esistono.
                totale_vendite = sum(importi_vendita) #fa la somma degli importi inseriti
                media_vendite = totale_vendite / len(importi_vendita) #calcola la media delle vendite , dividendo la somma per il numero di elementi nella lista
                print(f"Totale vendite: {totale_vendite}")            #len(importi_vendita) conta quanti importi sono stati inseriti
                print(f"Media vendite: {media_vendite:.2f}")
            else:
                print("Non ci sono vendite inserite.")

        elif scelta == 3: #esce dal ciclo e termina il menù
            print("Uscita dal menu vendite.")
            break

        else: 
            print("Scelta non valida, riprova.") #stampa se viene scelta un opzione non presente nel menu
            
menu_vendite()


