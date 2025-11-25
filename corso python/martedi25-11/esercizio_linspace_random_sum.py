import numpy as np

# Crea un array di 12 numeri equidistanti tra 0 e 1
arr = np.linspace(0, 1, 12)
print("array:", arr)

# Cambia la forma dell’array in una matrice 3x4
matrice = arr.reshape(3, 4)
print("array convertito in matrice:", matrice)

# Genera una matrice 3x4 di numeri casuali tra 0 e 1 (0 o 1 interi)
matrice_random = np.random.rand(3, 4)
print("Matrice random 3x4:", matrice_random)

# Calcola la somma degli elementi della matrice creata da linspace
sum_matrice = np.sum(matrice)
print("Somma Matrice:", sum_matrice)

# Calcola la somma degli elementi della matrice casuale
sum_matrice_random = np.sum(matrice_random)
print("Somma Matrice random:", sum_matrice_random)
