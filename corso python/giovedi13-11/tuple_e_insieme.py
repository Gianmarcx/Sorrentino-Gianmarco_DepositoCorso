#le tuple strutture di dati simili alle liste ma immutabili.

punto = (3,4)
colore_rgb = (255.128,0)
informazioni_persona = ("Alice",25,"Femmina")

#si può accedere agli elementi di una tupla usando l'indice dell'elemento desiderato

punto = (3,4)
print(punto[0])#output 3
print(punto[1])#output 4

#in alcuni casi si può creare una tupla senza l'uso delle (), questo è noto come tuple packing/unpacking.

punto = 3,4 #tuple packing
x , y = punto#tuple unpacking
print(x , y) #output 3 , 4

#INSIEMI: Sono una struttura dati che rappresenta una collezione non ordinata e senza duplicati di elementi 

set1 = set([1 , 2 , 3 , 4 , 5])
set2 = {4 , 5 , 6 ,7 ,8}

#non avendo duplicati se si prova ad aggiugerne uno , questo verrà ignorato. Gli indici iniziano da zero.

set3 = {1, 2 , 3 , 4 , 5}
print(set3) #output:{1, 2, 3, 4, 5}

#inoltre supportano varie operazioni , sono 4:

#Unione (union() o |): restituisce un nuovo insieme contenente tutti gli elementi presente in entrambi gli insiemi

#Intersezione (intersection() o &):restituisce



set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}

print(set1.union(set2)) #output {1,2,3,4,5,6,7,8}
print(set1.intersection(set2)) #output {4.5}
print(set1.difference(set2)) #output: {1,2,3}
print(set1.symmetric_difference(set2)) #output: {1,2,3,6,7,8}

#add() aggiungi un elemento ad un insieme
#remove() o discard() per rimouovere un elemento , la differenza sta nel fatto che remove genera un errore se l'elemento non è presente nell'insieme
#len() restituisce il numero di elementi presenti nell'insieme

print(set1.add(set2))
print(set1.remove(2))
print(set1.len())

#per verificare se è un elemento è presente nell'insieme usiamo l'operatore in
#con copy() possiamo creare la copia di un insieme , questa copia sarà indipendente dall'insieme originale

if 3 in set1:
    print("presente")

print(3 in set1)

set2= set1.copy()
print("Copia di set1:", set2)

