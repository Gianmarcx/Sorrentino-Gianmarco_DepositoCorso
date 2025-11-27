#Indicizzazione avanzata: Pandas permette un indicizzazione flessibile e sofisticata facilitanto l'accesso ai dati e la loro manipolazione
#Esempio di MultiIndex(indici gerarchici) consente di lavorare con dati ad alta dimensionalità in strutture tabulari bidimensionali

#Unione e Concatenazione: è possibile combinare facilmente diverse fonti di dati attraverso operazioni come merge per unire Dataframe simili a un joinSQL
#o concat per concatenare DataFrame lungo un asse specifico, gestendo anche indici che non si allineano


#RESISTIMAZIONE E PIVOT: pivot e pivot_table sono due metodi potenti che permettono di trasformare i dati
#facilitando la ristrutturazione e la creazione di tabelle pivot. Utile per riorganizzare i dati in un formato più apporpriato per l'analisi specifica

#GroupBy: Permette di dividere i dati in gruppi, applicare una funzione a ciascin gruppo indipendetemente , e combinare i risultati in una struttura di dati.
#Estremamente utile per aggregazioni complesse , trasformazioni e filtraggi

#Gestione del tempo: Pandas offre una funzionalità per la manipolazione delle serie temporali, che includono la generazioni di periodi di tempo,
#la conversione di frequenze , il windowing o il rolling statistics, e la manipolazione di date e orari

#ESEMPIO PRATICO USO DI pivot_table

import pandas as pd

#Dati di esempio 

data = {
    'Data': ['2021-01-01', '2021-01-01', '2021-01-01', '2021-01-02', '2021-01-02'],
    'Città': ['Roma', 'Milano', 'Napoli', 'Roma', 'Milano'],
    'Prodotto': ['Mouse', 'Tastiera', 'Mouse', 'Tastiera', 'Mouse'],
    'Vendite': [100, 200, 150, 300, 250]
}

df = pd.DataFrame(data)

#Creazione della tabella pivot
pivot_df = df.pivot_table(values='Vendite', index='Prodotto', columns='Città', aggfunc='mean')

print(pivot_df)



#Esempio pratico groupby

import pandas as pd

#Dati di esempio 

data = {
    'Data': ['2021-01-01', '2021-01-01', '2021-01-01', '2021-01-02', '2021-01-02'],
    'Città': ['Roma', 'Milano', 'Napoli', 'Roma', 'Milano'],
    'Prodotto': ['Mouse', 'Tastiera', 'Mouse', 'Tastiera', 'Mouse'],
    'Vendite': [100, 200, 150, 300, 250]
}

df = pd.DataFrame(data)

#Utilizzo di groupby per aggregare i dati
grouped_df = df.groupby('Prodotto').sum()

print(grouped_df)


#Manipolazione dei Dati: Include funzioni per modificare l'ordine dei dati, combinarli con altri set di dati o cambiare la loro struttura organizzativa

#Ordinamento dei datiper età
df_sorted = df.sort_values(by = 'età')

#Unione dei due dataframe
merged_df = pd.merge(df, df_csv, on = 'nome')

