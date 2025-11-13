#Esercizio 1: Inserisci un numero , se è pari stampa "Numero Pari" se dispari stampa "Numero Dispari"
numero = int(input ("Inserisci un numero"))

if numero % 2 == 0: #controlla se il numero è pari
    print("Numero Pari")
    
if numero % 2 != 0: #controlla se il numero è dispari
    print("Numero Dispari")
    
#Esercizio 2:

n = int(input("Inserisci un numero intero positivo:")) #inserisci un numero positivo

while True: #se il numero è appunto positivo allora stampa tutti i numeri partendo da quello inserito togliendo 1 fino ad arrivare a -1 ovvero 0
    for i in range (n, -1,-1): 
     print(i)
     
#Esercizio 3 

    lista_numeri = input("Inserisci i numeri:") #prende in input una lista di numeri
    
    numeri = [int(n) for n in lista_numeri.split()] #trasforma ogni elemento in un numero intero e li divide in una lista con spazi 
    
    print("Ecco la lista dei tuoi numeri:", numeri)
    
    for n in numeri: #ciclo for controlla ogni numero della lista 
        print(f"Il quadrato di {n} è {n**2}") #mostra il quadrato di ogni numero 
        
#Esercizio 4

    numeri = [int(n) for n in input("Inserisci numeri interi separati da spazio: ").split()] #prende i numeri interi e li divide in una lista con spazi 
    
    if len(numeri) == 0: #controlla se la lista è vuota e nel caso stampa "lista vuota"
        print("Lista vuota")
        
    else:
        #ciclo for per trovare il numero massimo della lista 
        massimo = numeri[0]
        for n in lista_numeri:
            if n > massimo:
                massimo = n
    
    #ciclo while che conta gli elementi 
    conta = 0 #conta i numeri partendo dal primo elemento con indice 0
    i = 0 #scorre la lista partendo da elemento 0
    while i < len(numeri):
        conta += 1
        i += 1
        
    print("Numero massimo:", massimo)
    print("Numeri nella lista:", conta)
     