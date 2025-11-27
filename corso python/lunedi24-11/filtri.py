#filter() funzione che permette di filtrare gli elementi dentro una sequenza 
#funziona_di_filtro è una funzione che accetta un argomento e restituisce True o False a seconda che l'elemento debba essere incluso o escluso dalla sequenza risultante
#può essere definita con def , ma è comune usare lamba function , per definireuna funzione di filtro semplice e concisa direttamente nell'argomento della funzione filter()

#In questo caso, abbiamo definito una funzione chiamata is_even(x) 
#che restituisce True se x è un numero pari e False altrimenti. 
# La funzione filter() applica questa funzione di filtro is_even a ciascun elemento della lista numbers e restituisce solo gli elementi che soddisfano la condizione, cioè i numeri pari. 
# Abbiamo definito una funzione regolare is_even() e l'abbiamo passata come primo argomento alla funzione filter(). La funzione filter() esegue automaticamente la chiamata is_even (x) per 四 ogni elemento x nella sequenza numbers e restituisce un iteratore con i soli elementi che soddisfano la condizione. Infine, abbiamo utilizzato la funzione List() per convertire l'iteratore restituito da filter() in una lista contenente i numeri pari filtrati

def is_even(x):
    return x % 2 == 0 

numbers = [1,2,3,4,5,6,7,8,9,10]
even_numbers = list(filter(is_even,numbers))
print(even_numbers) #output [2,4,6,8,10]


