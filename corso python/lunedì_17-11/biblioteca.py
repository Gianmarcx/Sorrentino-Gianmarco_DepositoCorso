class Biblioteca:
        def __init__(self):
            self.libri=[]
            
        def aggiungi_libro(self,titolo):
            self.libri.append((titolo))

        def stampa_libro(self):
            for titolo in self.libri:
                print(titolo)
                
        Biblioteca = Biblioteca()
        
        while True:
            titolo = input("n\Titolo")
            if titolo == "":
                break
            Biblioteca.crea_libro(titolo)
            
            
        print("Catalogo:")
        Biblioteca.stampa_libri()