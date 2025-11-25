import numpy as np

while True:  # Ciclo infinito: mostra il menu finché l'utente non sceglie di uscire
    print("\n--- MENU ---")
    print("1. Crea nuova matrice")
    print("2. Esci")
    scelta = input("Scegli un'opzione (1 o 2 ): ")  # Legge la scelta dell'utente

    if scelta == "1":  # Se l'utente vuole creare una nuova matrice
        # Chiede dimensioni e range dei numeri casuali
        scelta_colonna = int(input("Quante colonne vuoi?: "))
        scelta_righe = int(input("Quante righe vuoi?: "))
        num_min = int(input("Che numero minimo vuoi?: "))
        num_max = int(input("Che numero massimo vuoi?: "))

        # Crea una matrice 2D di dimensione (righe, colonne) con numeri interi casuali nel range [num_min, num_max)
        matrice2D = np.random.randint(num_min, num_max, size=[scelta_righe, scelta_colonna])
        print("Matrice:\n", matrice2D)

        # Salva la matrice sul file (in modalità 'w' sovrascrive il contenuto esistente)
        with open("corso python/martedi25-11/matrice2D.txt", "w") as f:
            f.write(str(matrice2D))

        # Calcola l'indice della riga centrale (divisione intera per trovare il centro)
        righe = matrice2D.shape[0]  # Numero di righe
        indice_riga_centrale = righe // 2
        riga_centrale = matrice2D[indice_riga_centrale]  # Estrae la riga centrale
        print("Colonna centrale:", riga_centrale)  # Nota: in realtà è una riga centrale, non colonna

        # Aggiunge (append) la riga centrale al file
        with open("corso python/martedi25-11/matrice2D.txt", "a") as f:
            f.write("\nRiga centrale:\n" + str(riga_centrale))

        # Calcola la trasposta (righe diventano colonne e viceversa)
        matrice2D_trasposta = matrice2D.T
        print("Matrice Trasposta:\n", matrice2D_trasposta)

        # Salva la trasposta nel file (in append)
        with open("corso python/martedi25-11/matrice2D.txt", "a") as f:
            f.write("\nMatrice trasposta:\n" + str(matrice2D_trasposta))

        # Calcola la somma di tutti gli elementi della matrice
        somma_matrice2d = np.sum(matrice2D)
        print("Somma totale matrice:", somma_matrice2d)

        # Salva la somma nel file
        with open("corso python/martedi25-11/matrice2D.txt", "a") as f:
            f.write("\nSomma totale:\n" + str(somma_matrice2d))
            
        # Crea una seconda matrice con lo stesso numero di righe e colonne della prima,
        # ma con un range di numeri casuali separato
        num_min_2 = int(input("Che numero minimo vuoi?: "))
        num_max_2 = int(input("Che numero massimo vuoi?: "))
        seconda_matrice2D = np.random.randint(num_min_2, num_max_2, size=matrice2D.shape)
        print("Seconda Matrice:\n", seconda_matrice2D)
        
        # Salva la seconda matrice nel file (append)
        with open("corso python/martedi25-11/matrice2D.txt", "a") as f:
            f.write("\nSeconda Matrice:\n" + str(seconda_matrice2D))
        
        # Moltiplicazione elemento per elemento (stesse dimensioni richieste)
        ElementWise = np.multiply(matrice2D , seconda_matrice2D)
        print("Moltiplicazione Element Wise delle Matrici:" , ElementWise)
        
        # Salva il risultato della moltiplicazione nel file
        with open("corso python/martedi25-11/matrice2D.txt", "a") as f:
            f.write("\nMoltiplicazione Element Wise delle matrici:\n" + str(ElementWise))
        
        # Calcola la media degli elementi della prima matrice
        media_matrice2d = np.mean(matrice2D)
        print("Media prima matrice:" , media_matrice2d)
        
        # Salva la media della prima matrice
        with open("corso python/martedi25-11/matrice2D.txt", "a") as f:
            f.write("\nMedia prima matrice:\n" + str(media_matrice2d))
        
        # Calcola la media degli elementi della seconda matrice
        media_seconda_Matrice2D = np.mean(seconda_matrice2D)
        print("Media seconda matrice:" , media_seconda_Matrice2D)
        
        # Salva la media della seconda matrice
        with open("corso python/martedi25-11/matrice2D.txt", "a") as f:
            f.write("\nMedia seconda matrice:\n" + str(media_seconda_Matrice2D))
            
            
    elif scelta == "2":  # Se l'utente sceglie di uscire
        print("Uscita dal programma. Alla prossima!")
        break  # Interrompe il ciclo while e termina il programma
    else:
        print("Scelta non valida. Riprova.")  # Gestione input non validi