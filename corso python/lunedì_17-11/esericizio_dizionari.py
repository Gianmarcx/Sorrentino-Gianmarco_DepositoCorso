lista = []

booleano = input("Inserisci un booleano(true/false):").lower() =="true"
intero = int(input("Inserisci un numero intero:"))
stringa = input("Inserisci una stringa:")

dati2 = {
    "numero":intero,
    "booleano":booleano,
    "stringa":stringa
     
    }

lista = [dati2]

dati = {
    "tipidato": [booleano,intero,stringa],
    "dizionati": lista
}

print(dati)

dizionario = {"tipididato": lista}

print(dizionario)