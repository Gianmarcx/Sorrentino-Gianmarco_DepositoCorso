#il brodcasting è una potenze funzione che permette di eseguire operazioni aritmetiche su array di forme diverse.
#questo riduce la necessità di creare array esplicitamente di dimensioni compatibili per le operazioni

#I PRINCIPI DEL BRODCASTING:

#Allinemento delle dimensioni : Quando NumPy esegue operazioni su due array, verifica se le loro dimensioni sono compatibili.
#Due dimensioni sono compatibili se:

#sono uguali
#una delle due dimensioni è 1 

#Espansione delle Dimensioni: Se le dimensioni non sono compatibili, NumPy espande le dimensioni di uno degli array automaticamente.ù
#L'array con la dimensione 1 viene espanso per avere la stessa dimensione dell'altro array.

#Applicazione dell'Operazione: Una volta che gli array hanno dimensioni compatibili, NumPy esegue l'operazione element-wise. 
# L'array più piccolo viene replicato per riempire l'array più grande.

import numpy as np

arr = np.array([1,2,3,4])
scalar = 10

#Brodcasting aggiunge lo scalare a ogni elemente dell'array
result = arr + scalar
print(result) #output [11 12 13 14]

#In questo esempio , lo scalare 10 viene brodcasted per avere la stessa dimensioen dell'array arr


#EFFICIENZA : Evita la necessità di creare copie esplicite di array per adattarne le dimensioni,
#riducendone il consumo di memeoria e migliorando le prestazioni

#SEMPLICITA': Rende il codice più leggibile e conciso, elimando così la necessità di scrivere loop espliciti per opeazioni element-wise



#REGOLE DI BRODCASTING


