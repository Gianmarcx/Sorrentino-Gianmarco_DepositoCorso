#SQL3:

#Un database è un insieme organizzato di dati strutturati e correlati tra loro, progettato per essere facilmente accessibile , gestito e aggiornato.

#ESISTONO VARI TIPI DI DATABASE: 

#- Database relazionali (RDBMS)
#Database non relazionali(NoSQL)


#Sqlite3 in python:

#In python sqlite3 è un modulo integrato nella libreria standard che ci permette 



#CRUD: Acronimo che rappresenta le 4 operazioni fondamentali per eseguire un insieme di dati su un sistema informatico: Create , Read , Update e Delete.






import sqlite3

#Connessione al database
conn = sqlite3.connect('esempio.db')
cur = conn.cursor()

#query con filtro(voto maggiore di 25)
cur.execute("SELECT nome, voto FROM studenti WHERE voto >?",(25,))

#Recupero dei risultati
studenti_meritevoli = cur.fetchall()

#Stampa dei risultati filtrati
for nome , voto in studenti_meritevoli:
    print(f"{nome} ha preso {voto}")
    
#chiusura della connesssione
conn.close()

#Questo script , serve per connettersi al database esempio.db
#Esegue una SELECT con filtro sulla colonna voto
#Recupera e stampa solo i nomi e voti degli studenti che hanno ottenuto più di 25



 #METODI PRINCIPALI DI sqlite3
 
