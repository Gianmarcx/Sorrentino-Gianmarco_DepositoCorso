class Punto:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def muovi(self):
        dx_sx = input("Dove vuoi spostarlo? (dx o sx): ").lower()
        
        if dx_sx == "dx":
            qnt = int(input("Di quante celle?: "))
            self.x += qnt
        else:
            qnt = int(input("Di quante celle?: "))
            self.x -= qnt

    def distanza_da_origine(self):
        return f"La distanza del punto è di {self.x} sull'asse x e {self.y} sull'asse y"


p1 = Punto(3, 4)
print(p1.distanza_da_origine())

p1.muovi()
print(p1.distanza_da_origine())
