import pandas as pd
import numpy as np

# 1. Carico il dataset
file_path = 'corso python/giovedi27-11/prove_pandas/dataset_clienti.csv'
df = pd.read_csv(file_path)

print("DataFrame originale:")
print(df.head())  # mostro solo le prime righe

# 2. Esplorazione iniziale
df.info()
print(df.describe())
print("\nValori di Churn:")
print(df['Churn'].value_counts())

# 3. Rimozione duplicati
df = df.drop_duplicates()

# 4. Gestione valori mancanti)
df['Età'].fillna(df['Età'].mean(), inplace=True)
df['Durata_Abbonamento'].fillna(df['Durata_Abbonamento'].mean(), inplace=True)
df['Tariffa_Mensile'].fillna(df['Tariffa_Mensile'].mean(), inplace=True)
df['Dati_Consumati'].fillna(df['Dati_Consumati'].mean(), inplace=True)
df['Servizio_Clienti_Contatti'].fillna(df['Servizio_Clienti_Contatti'].mean(), inplace=True)

# Elimino eventuali righe ancora incomplete
df = df.dropna()

# 5. Correzione anomalie (valori fuori scala)
df = df[(df['Età'] > 0) & (df['Età'] <= 110)]
df = df[df['Tariffa_Mensile'] >= 0]

# 6. Creazione nuova colonna: costo per GB
df['Costo_per_GB'] = df['Tariffa_Mensile'] / df['Dati_Consumati']

print("\nDataFrame con nuova colonna Costo_per_GB:")
print(df.head())

# 7. Analisi con groupby
print("\n--- Età media per Churn ---")
print(df.groupby('Churn')['Età'].mean())

print("\n--- Durata media abbonamento per Churn ---")
print(df.groupby('Churn')['Durata_Abbonamento'].mean())

print("\n--- Tariffa mensile media per Churn ---")
print(df.groupby('Churn')['Tariffa_Mensile'].mean())

print("\n--- Costo per GB medio per Churn ---")
print(df.groupby('Churn')['Costo_per_GB'].mean())

# 8. Matrice di correlazione
correlazione = df.corr(numeric_only=True)
print("\n--- Matrice di correlazione ---")
print(correlazione)

# 9. Conversione di Churn in numerico
df['Churn'] = df['Churn'].replace({'No': 0, 'Si': 1})

print("\n--- Churn convertito in numerico ---")
print(df['Churn'].value_counts())
print(df.dtypes)

# 10. Normalizzazione delle colonne numeriche (Min-Max scaling)
colonne = ['Età', 'Durata_Abbonamento', 'Tariffa_Mensile', 'Dati_Consumati', 'Servizio_Clienti_Contatti']

for col in colonne:
    df[col + '_norm'] = (df[col] - df[col].min()) / (df[col].max() - df[col].min())

print("\nDataFrame con colonne normalizzate:")
print(df.head())
