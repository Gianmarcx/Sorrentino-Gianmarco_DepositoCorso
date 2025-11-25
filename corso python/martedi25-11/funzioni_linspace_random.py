#linspace : genera un array di numeri equidistanti tr un valore iniziale e uno finale

import numpy as np

arr = np.linspace(0,1,5)
print(arr) #output(0. 0.25 0.5 0.75 1.)



#random: il modulo random di NumPy permette di generare array di numeri casuali

random_arr = np.random.rand(3,3) #Matrice 3x3 con valori casuali uniformi tra 0 e 1 
print(random_arr)

#sum , mean , std: numpy fornisce diverse funzioni per eseguire operazioni matematiche sugli array

arr = np.array([1,2,3,4,5])

sum_value = np.sum(arr)
mean_value = np.mean(arr)
std_value = np.std(arr)

print("Sum:", sum_value) #output 15
print("Mean:", mean_value) #output 3.0
print("Standard Deviation:", std_value) #output 1.4142135623730951

