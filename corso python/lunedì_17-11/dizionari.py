#I dizionari in python sono una struttura dati che consente di memorizzare coppie di chiavie valori.
#Sono rappresent

#Si possono creare un dizionario assegnando un insieme di coppie chiave-valore a una variabile, le coppie chiave-valore sono separate da due punti: e le coppie fra loro dalle virgola

studente = {
    "nome": "Alice",
    "età": 20,
    "sesso": "Femmina"
}


studente["città"] = "Roma"
print(studente)

#fare attenzione alla semamntica

#

#keys() per ottenere una lista di tutte le chivi
#values() per ottenere una lista di tutti i valori
#items() per ottenere una lista di tutte le coppie chiavi-valori
#get() per ottenere il valore associato ad una chiave

studente = {
    "nome": "Alice",
    "età": 20,
    "sesso": "Femmina"
}

print(studente.keys())
print(studente.values())
print(studente.items())
studente.get("nome")
