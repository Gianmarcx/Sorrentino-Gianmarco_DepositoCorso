eta_giusta = 18 #età minima consentita

eta = int(input("Inserisci la tua età:")) #inserisci età

#controllo età inserita
if eta >= eta_giusta:
    print("Accesso consentito, buona visione!")
    
elif eta < eta_giusta:
    print("Accesso negato,non sei ancora maggiorenne!!")
