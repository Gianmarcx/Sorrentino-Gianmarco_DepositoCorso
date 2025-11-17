def inserisci_importi():
    while True:
        importi_vendita = input("Inserisci gli importi di vendita separati da uno spazio: ")

        if not importi_vendita.strip():
            print("Non sono stati inseriti importi, riprova.")
            continue

        importi_lista = importi_vendita.split()

        try:
            importi_interi = [int(float(x)) for x in importi_lista]
            print("Importi convertiti in interi:", importi_interi)
            return importi_interi  # restituisce la lista e esce dal ciclo
        except ValueError:
            print("Errore: sono ammessi solo numeri separati da uno spazio, riprova.")


def menu_vendite():
    importi_vendita = []  # Lista iniziale vuota

    while True:
        print("\n--- Menu Vendite ---")
        print("1. Inserisci nuove vendite")
        print("2. Mostra totale e media delle vendite")
        print("3. Esci")

        try:
            scelta = int(input("Quale opzione hai scelto: "))
        except ValueError:
            print("Devi inserire un numero valido.")
            continue

        if scelta == 1:
            # Richiamo della funzione di inserimento
            nuovi_importi = inserisci_importi()
            importi_vendita.extend(nuovi_importi)
            print("Vendite aggiornate:", importi_vendita)

        elif scelta == 2:
            if importi_vendita:
                totale_vendite = sum(importi_vendita)
                media_vendite = totale_vendite / len(importi_vendita)
                print(f"Totale vendite: {totale_vendite}")
                print(f"Media vendite: {media_vendite:.2f}")
            else:
                print("Non ci sono vendite inserite.")

        elif scelta == 3:
            print("Uscita dal menu vendite.")
            break

        else:
            print("Scelta non valida, riprova.")


# Avvio del menu
menu_vendite()
