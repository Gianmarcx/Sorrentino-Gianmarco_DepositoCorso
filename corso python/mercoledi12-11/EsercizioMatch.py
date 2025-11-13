#credenziali hardcoded
username_corretto = "gianmarco"
password_corretta="12345"

#input utente
username = input("inserire username")
password = input("inserire password")

#verifica credenziali

if username == username_corretto and password == password_corretta:
    print("Benvenuto, " + username + "!")

    
#modifica credenziali o aggiungi domanda segreta

    print("Imposta domanda segreta:")
    print("Scegli opzione:")
    print("1.colore preferito?")
    print("2. Genere musicale preferito?")

    scelta = input("Scegli 1 o 2:")

    if scelta == "1":
     risposta = input("Inserisci colore preferito")
     print("Risposta impostata con successo!")

    elif scelta == "2":
        risposta = input("Inserisci genere musicale preferito")
        print("Risposta impostata con successo!")
    
else:
    print("Credenziali errate!Login negato")