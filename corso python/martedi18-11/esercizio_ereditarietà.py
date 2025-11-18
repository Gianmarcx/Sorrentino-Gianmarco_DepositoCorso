#creazione classe Animale con attributi nome ed età
class Animale:
    def __init__(self,nome,età):
        self.nome = nome
        self.età = età
        
    def fai_suono(self): #creazione metodo fai suono
         print(f"{self.nome} fa suono generico.")
         
class Leone(Animale): #creazione di una sottoclasse con ereditarietà , che eredeita fai_suono() da Animale
    def alimentazione(self): #creazione metodo alimentazione 
        print(f"{self.nome} è carnivoro")
     
    def habitat(self): #creazione metodo habitat
        print(f"{self.nome} vive nella Savana")
        
class Coccodrillo(Animale): #creazione di una sottoclasse con ereditarietà , che eredeita fai_suono() da Animale
    def alimentazione(self): #creazione metodo alimentazione 
        print(f"{self.nome} è carnivoro")
        
    def habitat(self): #creazione metodo habitat
        print(f"{self.nome} vive in fiumi e laghi tropicali")
        
class Orso_Polare(Animale): #creazione di una sottoclasse con ereditarietà , che eredeita fai_suono() da Animale
    def alimentazione(self): #creazione metodo alimentazione 
        print(f"{self.nome} è carnivoro")
        
    def habitat(self): #creazione metodo habitat
        print(f"{self.nome} vive nel Circolo Polare Artico")

nome_leone = input("Inserisci il nome del leone: ") #chiede di inserire in input un nome da assegnare al leone 
eta_leone = int(input("Inserisci l'età del leone: ")) #assegna in input un eta per il leone
leone = Leone(nome_leone, eta_leone) #assegna i valori al leone

nome_coccodrillo = input("Inserisci il nome del coccodrillo: ") 
eta_coccodrillo = int(input("Inserisci l'età del coccodrillo: "))
coccodrillo = Coccodrillo(nome_coccodrillo, eta_coccodrillo)

nome_orso = input("Inserisci il nome dell'orso polare: ")
eta_orso = int(input("Inserisci l'età dell'orso polare: "))
orso_polare = Orso_Polare(nome_orso, eta_orso)


#chiamata ai metodi 
leone.fai_suono()
leone.alimentazione()
leone.habitat()

coccodrillo.fai_suono()
coccodrillo.alimentazione()
coccodrillo.habitat()

orso_polare.fai_suono()
orso_polare.alimentazione()
orso_polare.habitat()