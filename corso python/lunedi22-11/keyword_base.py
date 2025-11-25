#Le Keyword sono 8:

#ndarray : l'oggetto array multidimensionale principale di numpy che può contenere dati di un singolo tipo 
#gli array di NumPy sono più veloci ed efficienti in termine di memoria rispetto alle liste native di python
#è possibile creare array NumPy usando funzioni come np.array(), np.zeros() , np.arange() e np.linspace()

#dtype: Specifica il tipo di dato degli elementi di un array. I tipi di dato comuni sono int , float , bool

#shape: Restituisce le dimensioni di un array con 3 righe e 4 colonne , lo shape avrà (3,4)

#arange: Crea array con valori sequenziali , simile alla funzione range() ma restituisce un array invece di una lista

#reshape: Cambia la shape di un array senza modificarne i dati

#linspace: Genera un array di numeri equamente distribuiti tra un valore iniziale e un valore finale

#random : genere un array con valore casuale, incluse distribuzioni normali e uniformi

#sum , mean , std: Funzioni per calcolare rispettivamente la somma, la media e la deviazione standard degli elementi di un array


#ESEMPIO ndarray:

import numpy as np

arr = np.array([1,2,3,4,5]) #creazione di un array dimensionale
arr2d = np.array([1,2,3],[4,5,6]) #creazione array bidimensionale

#è possibile creare array NumPy usando funzioni come np.array(), np.zeros() , np.arange() e np.linspace()

# Creazione di un array
arr = np.array([1, 2, 3, 4, 5])

# Utilizzo di alcuni metodi
print("Forma dell'array:", arr.shape) # Output: (5,)
print("Dimensioni dell'array:", arr.ndim) # Output: 1
print("Tipo di dati:", arr.dtype) # Output: int64 (varia a seconda della piattaforma)
print("Numero di elementi:", arr.size) # Output: 5
print("Somma degli elementi:", arr.sum()) # Output: 15
print("Media degli elementi:", arr.mean()) # Output: 3.0
print("Valore massimo:", arr.max()) # Output: 5
print("Indice del valore massimo:", arr.argmax()) # Output: 4

#ESEMPI dtype e shape:

arr = np.array([1,2,3], dtype='int32')
print(arr.dtype) #output : int32

#shape:
arr = np.array([1,2,3], [4,5,6])
print(arr.shape) #output: (2,3)


#ESEMPI arange e reshape:

arr = np.arange(10)
print(arr) #outpu [0 1 2 3 4 5 6 7 8 9]

arr = np.arange(6)
reshaped_arr = arr.reshape((2,3))
print(reshaped_arr)

