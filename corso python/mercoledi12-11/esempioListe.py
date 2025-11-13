#Le liste in Python sono una delle strutture dati più comuni e versatili. Sono collezioni ordinate e mutabili di elementi, e possono contenere oggetti di tipi diversi.

numeri = [1,2,3,4,5]
nomi = ["Alice,Bob,Charlie"]
misto = ["1, due, True, 4.5"]

#Si può accedere a gli elementi di una lista usando l'indice dell'elemento desiderato

numeri = [1 , 2 , 3 , 4 , 5]
print (numeri[0]) #output 1
print(numeri[2]) #output 3

print(len(numeri))

numeri.append(6)
numeri.insert(2,10)
numeri.remove(1)

print(numeri)