#clausole dei cicli: la funzione type() si usa per determinare il tipo di un oggetto o di una variabile. Restituisce il tipo di dati dell'oggetto passato come argomento

#type() è utile quando si vuole verifare il tipo di un oggetto 

#istruzione break() si usa per interrompere l'esecuzione di un ciclo 
#il continue si usa per saltare il resto del blocco di codice all'interno di un ciclo e passa alla prossima iterazione

numeri = [1,2,3,4,5]


for numero in numeri:
    if numero == 3: 
        break 
print(numero)

for numero in numeri:
    if numero == 3:
        continue 
print(numero)


#pass si usa quando non si desidera eseguire alcuna azione all'interno di un ciclo.

for i in range(5):
    if i == 3:
        pass
    print(i)
    
#operatore * è noto come operatore "splat", si usa per espandere un iterabile (come una lista , una tupla o un range) in elementi separati.

numeri = [*range(1,11)]
print(numeri)
#output:[1,2,3,4,5,6,7,8]



