#programma che controlla se un numero è primo/pari o no.
lista_numeriPari = []#lista numeri pari 

numero = int(input("Inserisci un numero"))
if numero % 2 == 0:
        print("Il numero è pari")
        lista_numeriPari.append(numero)
        print("Numero pari aggiunto in:", lista_numeriPari)
else:
    print("Il numero non è pari")
    
print("Hai trovato 5 numeri pari")
print("Lista finale", lista_numeriPari)