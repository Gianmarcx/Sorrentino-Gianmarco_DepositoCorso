#Esercizio 1
somma = 0 #questa variabile somma controlla tutti i numeri inseriti
    
while True: #ciclo while infinito che si interrope solo una volta inserito lo 0
    numero = int(input("Inserisci un numero intero(0 termina):"))
    
    if numero == 0:
        break #se il numero è 0 il break interrompe il ciclo
    
    somma += numero # somma dei numeri inseriti 
    
print(f"La somma dei numeri inseriti é :{somma}") #risultato

#Esercizio 2 

parola = input("Inserire parola") #variabile parola che chiede di dare una parola come input

#ciclo for che stampa ogni lettera della prola inserita
for lettera in parola:
    print(lettera)
    
#Esercizio 3
N = int(input("Inserire numero massimo:")) #variabile N che chiede in input un numero massimo da inserire
steps = int(input("Inserire uno step:")) #variabile steps chiede di dare in input uno step come intervallo di stampa fino ad arrivare al numero massimo

for i in range(0,N+1,steps): #partendo da 0 arriva fino al numero massimo da noi inserito seguendo la step d'intervallo sempre da noi inserito
        print(i) #stampa il tutto