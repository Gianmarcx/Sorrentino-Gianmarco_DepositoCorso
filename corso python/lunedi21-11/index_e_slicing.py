#Index e slicig: Gli array NumPy possono essere indicizzati e affettati in modo simile alle liste python , ma con funzionalità aggiuntive 

import numpy as np

arr = np.array([1, 2, 3, 4, 5]) #creazione array

# Indexing
print(arr[0]) # Output: 1  Stampa elemento nella posizione 0 dell'array

# Slicing
print(arr[1:3]) # Output: [2 3] prende elementi da indice 1 a indice 2 

# Boolean Indexing
print(arr[arr > 2]) # Output: [3 4 5] #crea array con valori True/False , prende solo elementi dove c'è true


#gli array supportano slicing e fancy indexing permettono di estrarre porzioni di array e modificano il loro contenuto in modo efficiente

import numpy as np

# Creo un array 2D (una matrice)
arr_2d = np.array([
    [1,  2,  3,  4],
    [5,  6,  7,  8],
    [9, 10, 11, 12]
])

# Slicing sulle righe (prendo le righe 1 e 2 → la 3 non è inclusa)
print(arr_2d[1:3])
# Output:
# [[ 5  6  7  8]
#  [ 9 10 11 12]]


# Slicing sulle colonne (prendo tutte le righe ":" e le colonne 1 e 2)
print(arr_2d[:, 1:3])
# Output:
# [[ 2  3]
#  [ 6  7]
#  [10 11]]


# Slicing misto (righe da 1 in poi, colonne 1 e 2)
print(arr_2d[1:, 1:3])
# Output:
# [[ 6  7]
#  [10 11]]


#SLICING: Permette di estrarre una parte di array o di una sequenza , in NumPy lo slicing è simile a quelle delle liste in python
#ma è più potente e versatile

import numpy as np

print(arr[1:8:2]) #Slicing con passo: output [1 3 5 7]

print(arr[:5]) #output [0 1 2 3 4]
print(arr[5:]) #output [5 6 7 8 9]

#Fancy Indexing: Permette di selezionare elementi di un array usando array di indici interi
#queso consente una selezione complessa e flessibile di elementi rispetto allo slicing normale

arr = np.array([10,20,30,40,50])

#Utilizzo di un array di indici
indices = np.array([1,3])
print(arr[indices]) #output [20 40]

#Utilizzo di una lista di indici
indices = [0 ,2 , 4]
print(arr[indices]) #output [10 30 50]

#Differenze tra Slicing e F.Indexcing

#Slicing: è limitatlo a selezioni rettangolari , restituisce una vista dell'array originale(non crea una copia), usa indici di inzio, fine e passo

#Fancy Indexing: Può selezionare elementi non contigui e in ordine arbitrario , crea sempre una copia dei dati selezionati , usa array di indici interi

