# Creare una serie di condizioni una dentro l’altra che a fronte di un
#input per ogni if decidano se farti passare o no ( 3 livelli, fate un
#paragone con == )

lv1 = int(input("Inserisci primo numero: "))
if lv1 == 10:
    print("Step 1 superato")

    lv2 = int(input("Inserisci secondo numero: "))
    if lv2 == 20:
        print("Step 2 superato")

        lv3 = int(input("Inserisci terzo numero: "))
        if lv3 == 30:
            print("Step 3 superato - Accesso consentito!")
        else:
            print("Step 3 fallito!")
    else:
        print("Step 2 fallito!")
else:
    print("Step 1 fallito!")
10
    

#Andare a creare un if con vari elif e un else finale che gestisca un
#menu per la selezione di un crud basilare (aggiungi rimuovi elimina )   

print("****MENU CRUD****")
print("1. Aggiungi")
print("2. Visualizza")
print("3. Elimina")

scelta = int(input("scegli opzione (1-3):"))
if scelta == 1:
    print("Hai scelto Aggiungi")
elif scelta == 2:
    print("Hai scelto Visualizza")
elif scelta == 3:
    print("Hai scelto Elimina")
else:
    print("Opzione non trovata, riprova!")
