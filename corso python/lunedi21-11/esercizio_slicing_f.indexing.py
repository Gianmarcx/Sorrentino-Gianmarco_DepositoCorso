import numpy as np

# 1. Crea un array NumPy 1D di 20 numeri interi casuali tra 10 e 50
array1D = np.random.randint(10, 51, 20)
print("Array originale:", array1D)

# 2. Estrai i primi 11 elementi
print("Primi 11 elementi:", array1D[0:11])

# 3. Estrai gli ultimi 5 elementi
print("Ultimi 5 elementi:", array1D[-5:])

# 4. Estrai gli elementi da indice 5 a 14 (15 escluso)
print("Elementi da indice 5 a 14:", array1D[5:15])

# 5. Estrai ogni terzo elemento
print("Ogni terzo elemento:", array1D[::3])

# 6. Modifica gli elementi da indice 5 a 9 (10 escluso) con valore 99
array1D[5:10] = 99
print("Array dopo modifica:", array1D)




