#Pandas è una libreria che si usa per la manipolazione e l'analisi dei dati
#offre strutture di dati e operazioni per manipolare tabelle numeriche e serie temporali.
#è indispensabile nel campo del data science

#riprende il concetto di operazione vettoriale


#Pandas introduce due strutture dati fondamentali: DataFrame e Series

#DataFrame : Una struttura dati bidimensionale simile a un foglio di calcolo o a una tabella SQL.
#Composto da righe e colonne,dove ogni colonna può contenere dati di un tipo specifico(numerici,stringhe,booleani)

#Series: Una struttura dati unidimensionale che può essere vista come una colonna di DataFrame,
#Ogni series ha un solo tipo di dato




#per caricare i dati da un file csv utilizzando pandas, segue questo processo tipico per l'inizio di un analisi dei dati
#dove i dati vengono prima caricati in un DataFrame che è la struttura dati primaria in pandas

import pandas as pd #importazione di pandas

#Percorso del file CSV
file_path = 'corso python/giovedi27-11/prove_pandas/vendite.csv'  #specifica il percorso del file csv da caricare

#Caricamento dei dati nel dataframe
df = pd.read_csv(file_path) #metodo utilizzato per caricare i dati dal file csv

#le prime righe del DataFrame per confermare
print(df.head()) 


#Pandas apprezzato per diverse funzionalità chiave:

#Manipolazione dei dati: Permette di eseguire operazioni complesse su dati come selezione,filtraggio,fusione,raggruppamento , e reshaping dei dati con semplici comandi

#Pulizia dei dati: Offre molteplici funzioni per trattare dati mancanti, rimuovere duplicati, convertire formati di dati che sono essenziali per preparare i dataset per l'analisi

#Analisi dei dati: Supporto per operazioni come aggregazioni, sommatio statistico , e altre funzioni analitiche che facilitano l'estrarre insight dai dati

#Interoperabilità; Si integra bene con altre librerie per la visualizzazione dati(es. Matplotlib) e analisi statistica(es. SciPy)


#Pandas è fondamentale per l'analisi dei
#dati grazie alla sua versatilità e
#potenza.

#La libreria si distingue per la capacità
#di gestire facilmente dati mancanti,
#supportare formati diversi per
#l'importazione e l'esportazione di dati,
#e per la sua integrazione con altri
#pacchetti Python utilizzati per
#l'analisi e la visualizzazione dei dati.

#Le operazioni su DataFrame e Series sono
#ottimizzate per essere non solo
#intuitive ma anche veloci, supportando
#grandi volumi di dati con una sintassi
#chiara e leggibile.

import pandas as pd

# Creazione di un DataFrame con dati di esempio
data = {
    'Nome': ['Alice', 'Bob', 'Carla'],
    'Età': [25, 30, 22],
    'Città': ['Roma', 'Milano', 'Napoli']
}
df = pd.DataFrame(data)

# Stampa del DataFrame originale
print("DataFrame Originale:")
print(df)

# Selezione delle righe dove l'età è superiore a 23
df_older = df[df['Età'] > 23]

# Stampa delle righe selezionate
print("\nPersone con età superiore a 23 anni:")
print(df_older)

# Aggiungiamo una nuova colonna La persona maggiorenne
df['Maggiorenne'] = df['Età'] >= 18

# Stampa del DataFrame con la nuova colonna
print("\nDataFrame con colonna 'Maggiorenne':")
print(df)




#PULIZIA DEI DATI:

# Pandas
# La pulizia dei dati è un passaggio essenziale nel processo di analisi dei dati,
# specialmente quando si lavora con set di dati reali che spesso contengono valori
# mancanti, duplicati o errati.
# Pandas offre strumenti potenti per affrontare queste problematiche in modo efficiente.

import pandas as pd
import numpy as np

# DataFrame esempio, inclusi valori mancanti e duplicati
data = {
    'Nome': ['Alice', 'Bob', 'Carla', 'Bob', 'Carla', 'Alice', None],
    'Età': [25, 30, 22, 30, np.nan, 25, 29],
    'Città': ['Roma', 'Milano', 'Napoli', 'Milano', 'Napoli', 'Roma', 'Roma']
}
df = pd.DataFrame(data)

# Stampa del DataFrame originale
print("DataFrame Originale:")
print(df)

# Rimozione dei duplicati
df = df.drop_duplicates()

# Gestione dei dati mancanti

# Possiamo rimuovere le righe dove almeno un elemento è mancante
# df_cleaned = df.dropna()

# possiamo sostituire i dati mancanti con valore di default (media)
df['Età'].fillna(df['Età'].mean(), inplace=True)

# Stampa del DataFrame pulito
print("\nDataFrame dopo la pulizia:")
print(df)

# Stampa del DataFrame con dati mancanti sostituiti
print("\nDataFrame con dati mancanti sostituiti:")
print(df)

