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




#Serie Temporali: Pandas offre strumenti per manipolare date e tempi, permette di analizzare serie temporali, cambiare le frequenza dei dati e generare periodi di tempo

#Generazione di una serie di date
data_range = pd.date_range(start='2021-01-01' , periods=10, freq='M')

#Resampling dei dati di una serie temporale
df_resampled = df.resample('M').mean()


#pd.to_datetime() : converte un indice o una colonna in formato datetime, permettendo di sfruttare tutte le funzionalità di time series DI python

import pandas as pd

#esempio: colonna "date"in stringhe --> datetime
df['date'] = pd.to_datetime(df['date'], format= '%Y-%m-%d')
#oppure per creare un indice
df.index= pd.to_datetime(df['date'])

#DataFrame.resample() : Ridimensiona (aggregate o down/up-sample) la frequenza temporale dei dati specificanzo l'intervallo desiderato('D' = day, 'M'=month , 'H' = hour, ...)

#Partendo da un dataframe con indci DatetimeIndex
df_daily = df.resample('D').mean #media giornaliera
df_monthly = df.resample('M').sum() #somma mensile

#Series.shift() : "Sposta" i valori lungo l'asse temporale di un numero di periodi, utile per calcolare differenze ritardate , tassi di crescita , ecc.

#aggiunge una colonna con il valore del giorno precedente
df['prev_day'] = df['value'].shift(1)

#tasso di variazione giornaliero
df['daily_return'] = df['value'].pct_change()
#equivalente a shift + calcolo%

