#Numpy include il modulo per l'algebra lineare(numpy.linalg) che supporta operazioni come:

#Prodotto Matriciale: np.dot(), np.matmul()

import numpy as np

a = np.array([[1,2], [3,4]]) #creazione di una matrice quadrata

a_inv = np.linalg.inv(a) #calcolo dell'inversa della matrice
print("Inversa di A:\n", a_inv)

#Esempio 2: Norma di un Vettore 

import numpy as np

v = np.array([3,4]) #creazione di un vettore

#calcolo della norma del vettore

norm_v = np.linalg.norm(v)
print("Norma di v:" , norm_v) #output 5.0


#numpy.linalg.solve : funzione utilizzata per risolvere un sistema lineare di equazioni della forma Ax=Bx = BAx=B , dove AAA è uan matrice quadrata
#e BBB è un vettore o una matrice

import numpy as np

#Creazione della matrice A e del vettore B
A = np.array([[3,1],[1,2]])
B = np.array([9,8])

#Risoluzione del sistema di equazioni Ax = B
x = np.linalg.solve(A , B)
print("Soluzione x: ",x) #output [2. 3.]

#numpy.ftt.ftt Questa funzione calcola la Trasformata di Fourier Discreta (DFT) di un array. 
#La DFT è uno strumento potente per analizzare le frequenze dei segnali.

import numpy as np
 
 # Creazione di un segnale
t = np.linspace(0, 1, 400)
sig = np.sin(2 * np.pi * 50 * t) + np.sin(2 * np.pi * 120 * t)
 
 # Calcolo della Trasformata di Fourier
fft_sig = np.fft.fft(sig)
 
# Frequenze associate
freqs = np.fft.fftfreq(len(fft_sig))
 
print("Trasformata di Fourier:", fft_sig)
print("Frequenze associate:", freqs)