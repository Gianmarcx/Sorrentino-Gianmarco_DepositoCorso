import numpy as np  # Importa la libreria NumPy, utile per lavorare con array numerici

# Crea un array con valori da 0 a 49 (totale 50 elementi)
array = np.arange(50)

# Genera 50 numeri interi casuali tra 40 e 101 (102 è escluso)
array_casuale = np.random.randint(40, 102, size=50)

# Unisce i due array in uno solo da 100 elementi
ndarray = np.concatenate((array, array_casuale))

# Stampa l'array completo, il suo tipo di dato e la forma (numero di elementi)
print("Array:", ndarray)
print("dtype:", ndarray.dtype)      # Tipo di dato (es. int64)
print("shape:", ndarray.shape)      # Forma: (100,) → 100 elementi in 1 dimensione

# Converte l'array in float64 (numeri con virgola) e verifica
ndarray_float = ndarray.astype(np.float64)
print("dtype post conversione:", ndarray_float.dtype)
print("shape:", ndarray_float.shape)

# ---- SLICING (estrazioni con indici) ----

# Primi 10 elementi: indici da 0 a 9
print("Primi 10 elementi:", ndarray[0:10])

# Ultimi 7 elementi: parte dalla fine (dal -7 fino alla fine)
print("Ultimi 7 elementi:", ndarray[-7:])

# Elementi dall'indice 5 al 19 (20 escluso)
print("Elementi da indice 5 a indice 20 (escluso):", ndarray[5:20])

# Ogni quarto elemento, partendo dall'inizio (passo = 4)
print("Ogni quarto elemento:", ndarray[::4])

# ---- Modifica con slicing ----

# Assegna il valore 999 agli elementi con indici 10,11,12,13,14 (15 escluso)
ndarray[10:15] = 999
print("Array post modifica:", ndarray)

# ---- Fancy indexing (selezione con lista di indici) ----

# Definisce le posizioni da estrarre
index = [0, 3, 7, 12, 25, 33, 48]

# Seleziona gli elementi in quelle posizioni
posizioni = ndarray[index]
print("Elementi in posizione [0, 3, 7, 12, 25, 33, 48]:", posizioni)

# ---- Maschere booleane ----

# Seleziona tutti gli elementi pari (resto della divisione per 2 uguale a 0)
elementi_pari = ndarray[ndarray % 2 == 0]
print("Elementi pari:", elementi_pari)

# Calcola la media dell'array e seleziona gli elementi maggiori della media
media = ndarray.mean()
elementi_maggiori_della_media = ndarray[ndarray > media]
print("Elementi maggiori della media (media =", media, "):", elementi_maggiori_della_media)
