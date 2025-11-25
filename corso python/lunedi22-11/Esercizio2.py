import numpy as np

# 1. Crea una matrice 6x6 con numeri casuali tra 1 e 100
matrice2D = np.random.randint(1, 101, size=(6, 6))
print("Matrice 6x6 casuale:")
print(matrice2D)

# 2. Estrai la sotto-matrice centrale 4x4
estrazione_4x4 = matrice2D[1:5, 1:5]
print("\nSotto-matrice centrale 4x4:")
print(estrazione_4x4)

# 3. Inverti le righe della sotto-matrice
matrice_invertita = estrazione_4x4[::-1, :]
print("\nMatrice invertita (righe invertite):")
print(matrice_invertita)

# 4. Estrai la diagonale principale e crea un array 1D
diagonale = np.diag(matrice_invertita)
array1D = np.array(diagonale)
print("\nDiagonale principale (array 1D):")
print(array1D)

# 5. Sostituisci i multipli di 3 con -1
matrice_modificata = matrice_invertita.copy()
matrice_modificata[matrice_modificata % 3 == 0] = -1
print("\nMatrice invertita con multipli di 3 sostituiti da -1:")
print(matrice_modificata)
