#ciclo matematico con while, il while si uda per eseguire un blocco di codice finchè una determinata condizione è vera

conteggio = 0 
    
while conteggio < 5:    
    print(conteggio)
    conteggio += 1 

#ciclo booleano

controllo = True

while controllo:
    print(controllo)#cosi si ripeterà infinite volte
    #in questo modo non sarà più infinito
    scelta = input("vuoi continuare?")
    if scelta.lower() == "no":
        controllo= False
    else:
        print("stai continuando")
 
x = 0

#ciclo matematico

while x < 5:
    x+=1
    print(x)   
