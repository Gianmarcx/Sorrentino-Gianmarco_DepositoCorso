import numpy as np

arr = np.arange(10,50) #funzione np.arange per creare numeri interi da 10 a 49
print(arr) #stampa l'array
print("Tipo di dato:" , arr.dtype) #mostra il tipo di dato dell'array
print("Forma array:" , arr.shape)#stampa la forma dell'array

arr_float = np.array([float(x) for x in arr ]) #converte i numeri dell'array in float
print(arr_float) #stampa il risultato

print("Tipo di dato:" , arr.dtype) #mostra il tipo di dato dell'array
print("Forma array:" , arr.shape)#stampa la forma dell'array