primo_numero = int(input("Inserisci primo numero:")) 
secondo_numero = int(input("Inserisci secondo numero:"))

#Menu per scelta operazioni
print("MENU OPERAZIONI")
print("1. addizione")
print("2. sottrazione")
print("3. moltiplicazone")
print("4. divisione")

scelta = int(input("Quale operazione scegli:"))

#concatenazione di if , elif ed else per i mostrare i risultati dell'operazione scelta in precedenza
if scelta == 1:
        print(primo_numero + secondo_numero) #risultato addizione
        
elif scelta == 2:
    print(primo_numero - secondo_numero) #risultato sottrazione
    
elif scelta == 3:
    print(primo_numero * secondo_numero) #risultato moltiplicazione
    
elif scelta == 4:
    if secondo_numero == 0:
        print("Impossibile dividere per 0") #errore impossibile dividere per zero
        
    else:
        print(primo_numero / secondo_numero) #risultato divisione
    
    
