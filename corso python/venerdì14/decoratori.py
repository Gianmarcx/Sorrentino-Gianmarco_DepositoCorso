#I decoratori in Python sono una funzione che modifica il comportamento di un'altra funzione o metodo senza modificarne direttamente il codice. Si utilizzano spesso per aggiungere funzionalità extra come logging, controllo degli accessi, caching, e altro. Si applicano anteponendo il simbolo @ al nome del decoratore sopra la funzione da decorare

def decoratore(funzione):
    def wrapper():
        print("Prima dell'esecuzione della funzione")
        funzione()
        print("Dopo l'esecuzione della funzione")
        return wrapper
    
@decoratore
def saluta():
    print("Ciao!")
    
    saluta()

#funzioni che modificano il comportamento di un'altra funzionalità senza modificare il codice di quella funzionalità
#si usa def nome decoratore("nome della funzione")

#un wrapper è una funzione interna definita all'interno di un decoratore che avvolge la funzione originale e permettere di aggiungere funzionalità extra primo o dopo l'esecuzione della funziona decorata, senza cambiare direttamente il codice

def decoratore_con_argomenti(funzione):
    def wrapper(*args,**kwargs):
        print("Prima")
        risultato = funzione(*args,**kwargs)
        print("Dopo")
        return risultato
    return wrapper

@decoratore_con_argomenti
def somma(a,b):
    print(a + b)
    return a + b

print("risultato è",somma(3,4))

# ilwrapper usa *args e *kwargs per garantire che possa gestire un numero variabile di argomenti posizionali e keyword mantenendo la flessibilità della funzione originale

#logger(funzione) decoratore che prende una funzione (ad esempio moltiplica) come input

#funzione wrappers *args e **kwargs : il decoratore crea una funzione interna che esegue il codice prima e dopo la chiamata alla funzione originale. In questo caso il wrapper stampa gli argomenti e il risultato della funzione decorata

#@logger: Questo applica il decoratore alla funzione moltiplica, ovvero che ogni volta che chiamiamo moltiplica verrà eseguito prima il codice che il wrapper


import time #importa modulo time necessario per misurare il tempo e usare time.sleep()


def calcola_tempo(funzione):#definisce il decoratore calcolo_tempo e prende come argomento una funzione che vogliamo decorare
    def wrapper(*args, **kwargs): #definisce la funzione wrapper , che sostituirà la funzione originale quando la decoriamo, *args **kwargs permettere alla funzione decorata di ricevere qualsiasi numero di argomenti
        start_time = time.time()
        risultato = funzione(*args, **kwargs)
        end_time = time.time()
        print(f"Tempo di esecuzione: {end_time - start_time} secondi")
        return risultato
    return wrapper

@calcola_tempo
def calcolo_lento():
    time.sleep(2)
    print("Calcolo completato")

# Chiamata alla funzione decorata
calcolo_lento()


