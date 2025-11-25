import numpy as np
# Importa NumPy, libreria per il calcolo numerico con array.

array = np.random.randint(1, 101, 15)
print(array)
# Crea un array di 15 interi casuali tra 1 e 100 (101 è escluso) e lo stampa.

sum = np.sum(array)
print("Somma:", sum)
# Calcola la somma di tutti gli elementi dell'array.

mean = np.mean(array)
print("Media:", mean)
# Calcola la media aritmetica degli elementi dell'array.

# ESERCIZIO 2 

matrice = np.arange(1, 26).reshape(5, 5)
print("Matrice:", matrice)
# Crea i numeri da 1 a 25 e li ridispone in una matrice 5x5.

colonna_estratta = matrice[:, 1]
print("colonna estratta:", colonna_estratta)
# Estrae la seconda colonna: ":" tutte le righe, "1" è l'indice della colonna (gli indici partono da 0).

riga_estratta = matrice[2]
print("Riga estratta:", riga_estratta)
# Estrae la terza riga: indice 2 perché si parte da 0.

# ESERCIZIO 3

arr = np.random.randint(10, 51, size=(4, 4))
print("Array 4x4:", arr)
# Crea una matrice 4x4 con interi casuali tra 10 e 50 (51 escluso).

righe = [0, 1, 2, 3]
colonne = [1, 3, 2, 0]
elementi = arr[righe, colonne]
print("Elementi selezionati:", elementi)
# Fancy indexing: seleziona gli elementi nelle posizioni (0,1), (1,3), (2,2), (3,0).
# Si passa una lista di indici di riga e una di colonna della stessa lunghezza.

righe_dispari = arr[1::2]
print("Righe dispari array:", righe_dispari)
# Estrae le righe con indici dispari (1 e 3): parte da 1 e prende una riga ogni 2.

scalar = 10
risultato = arr + scalar
print("Aggiunta valore 10:", risultato)
# Broadcasting: aggiunge 10 a TUTTI gli elementi della matrice (non solo a quelli selezionati).
