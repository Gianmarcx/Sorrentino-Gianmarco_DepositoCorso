import numpy as np

def leggi_dati(file_name="dati.txt"):
    try:
        with open(file_name, "r") as f:
            dati = [float(x) for x in f.read().split()]
        return np.array(dati)
    except FileNotFoundError:
        print(f"Il file {file_name} non esiste ancora.")
        return np.array([])


def salva_risultati(info, file_name="risultati.txt"):
    scelta = input("Vuoi sovrascrivere il file (w) o aggiungere (a)? [w/a]: ").lower()
    if scelta not in ["w", "a"]:
        print("Scelta non valida, imposto 'a' (aggiunta).")
        scelta = "a"

    with open(file_name, scelta) as f:
        if isinstance(info, list):
            for dato in info:
                f.write(str(dato) + "\n")
        else:
            f.write(str(info) + "\n")
    print(f"Risultati salvati in {file_name} (modo: {scelta})")


def salva_dati(arr, file_name="dati.txt"):
    scelta = input("Vuoi sovrascrivere il file (w) o aggiungere (a)? [w/a]: ").lower()
    if scelta not in ["w", "a"]:
        print("Scelta non valida, imposto 'a' (aggiunta).")
        scelta = "a"

    with open(file_name, scelta) as f:
        for valore in arr:
            f.write(str(valore) + "\n")
    print(f"Array salvato in {file_name} (modo: {scelta})")


def crea_array():
    print("\n=== CREA ARRAY ===")
    print("1. Linspace (numeri equidistanti)")
    print("2. Random (valori casuali tra 0 e 9)")

    scelta = input("Cosa vuoi creare? ")

    if scelta == "1":
        array = np.linspace(0, 10, 50)
    elif scelta == "2":
        array = np.random.randint(0, 10, 50)
    else:
        print("Scelta non valida, creo un array vuoto.")
        array = np.array([])

    print("Array creato:", array)
    return array


def calcola_array(arr):
    somma_totale = np.sum(arr)
    somma_maggiori_5 = np.sum(arr[arr > 5])
    print("Somma totale:", somma_totale)
    print("Somma elementi > 5:", somma_maggiori_5)
    return somma_totale, somma_maggiori_5



arr = crea_array()
somma_tot, somma_5 = calcola_array(arr)
salva_dati(arr)
salva_risultati([somma_tot, somma_5])
dati_letti = leggi_dati()
print("Dati letti:", dati_letti)
