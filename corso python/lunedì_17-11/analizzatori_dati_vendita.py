def inserisci_importi(): #definiamo la funziona inserisci_importi()
    while True: #ciclo while infinito fin quando non viene inserito un input giusto
        importi_vendita = input("Inserisci gli importi di vendita separati da uno spazio: ") #variabile che chiede di inserire in input degli importi di vendita separati da uno spazio

        if not importi_vendita.strip(): #segnala nel caso non siano stati inseriti importi
            print("Non sono stati inseriti importi, riprova.")
            continue #ricomincia il ciclo while

        importi_lista = importi_vendita.split() #divide la stringa in singoli elementi 

        try: #prova a convertire gli importi di vendita float in numeri interi 
            importi_interi = [int(float(x)) for x in importi_lista]
            print("Importi convertiti in interi:", importi_interi)
            return importi_interi  # restituisce la lista e esce dalla funzione
        except ValueError: #se uno degli elementi non è valido , stampa l'errore
            print("Errore: sono ammessi solo numeri separati da uno spazio, riprova.")


