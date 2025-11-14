
n = int(input("Inserisci un numero intero positivo")) #variabile n che chiede di inserire come input un numero intero positivo

while n <= 0: #ciclo while che si assicura che l'utente inserisca solo numeri interi positivi, altrimenti in caso contrario da Errore 
    print("ERRORE: inserisci solo numeri interi positivi!!!")
    n = int(input("Inserire numero intero positivo:"))
    
somma_numeri_pari = 0

for i in range(0,n+1):
    if i % 2 == 0:
        somma_numeri_pari += i 
print("Somma dei numeri pari:", somma_numeri_pari)
        
print("Numeri dispari:")
for i in range(0,n+1):
    if i % 2 != 0:
        print(i)

primo = True
                
if n == 1:
       primo = False
else:
    for i in range(2, n):
        if n % i == 0:
            primo = False
            break

if primo:
    print("Il numero è primo")
else:
    print("Il numero non è primo")      
       
