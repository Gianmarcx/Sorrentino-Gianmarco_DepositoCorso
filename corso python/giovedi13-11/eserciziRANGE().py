#esercizio conto alla rovescia
ripetizione = "si"

while ripetizione == "si":
    numero = int(input("Inserisci un numero:"))

#inizio contoa alla rovescia partendo da numero inserito fino ad arrivare a -1 , ovvero 0 
    print("Inizio conto alla rovescia")
    for i in range(numero,-1, -1):
        print(i)

#chiede se si vuole ripetere il conto alla rovescia , inserendo nuovamente un numero
    ripetizione = input("Vuoi ripetere? (si/no):")
    
    if ripetizione == "no":
        print("Stop")
        

    