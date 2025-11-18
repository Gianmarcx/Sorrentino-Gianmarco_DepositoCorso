class Libro:
    def __init__(self,titolo,autore,isbn):
        self.titolo = titolo
        self.autore = autore
        self.isbn = isbn
        
    def descrizione(self):
        return f"Titolo: {self.titolo}, Autore: {self.autore}, ISBN: {self.isbn}"
        

        
    class Libreria:
        def __init__(self):
            self.catalogo = []

    def aggiungi_libro(self,libro):
        self.catalogo.append(libro)
        print(f"Libro '{libro.titolo}' aggiunto al catalogo!")
        
    def rimuovi_libro(self,isbn):
        for libro in self.catalogo:
            if libro.isbn == isbn:
                self.catalogo.remove(libro)
                print(f"Libro con isbn '{isbn} rimosso!'")
                return
            print(f"nessun libro con isbn '{isbn}'trovato!")
            
    def mostra_catalogo(self):
        if not self.catalogo:
            print("Il catalogo è vuoto.")
        else:
            print("\nCatalogo libri:")
            for libro in self.catalogo:
                print(libro.descrizione())
        
        
                    
    
    
        