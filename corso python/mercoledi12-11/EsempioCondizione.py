#istruzione if usata per eseguire blocco di codice 

numero = 10
if numero> 0:
    print("il  numero è positivo")
    
#else usata per definire un blocco di codice da eseguire se le condizioni precedenti sono false

numero = 10
if numero> 0:
    print("il  numero è positivo")
else:
    print("Blocco Else")
    
#gli if sono annidabili, si può avere un if con dentro un altro if

        
numero = 10
if numero> 0:
    print("il  numero è positivo") 
    if numero == 100:
        print("wow")
elif numero < 0:
    print("Il numero è negativo")
    
else:
    print("il numero è zero")  
    
