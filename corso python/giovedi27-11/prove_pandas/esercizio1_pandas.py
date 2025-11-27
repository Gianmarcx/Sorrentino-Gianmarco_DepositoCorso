import pandas as pd
import numpy as np

# Percorso del file CSV (Titanic - train.csv)
file_path = 'corso python/giovedi27-11/prove_pandas/train.csv'

# 1) Carico il dataset in un DataFrame
df = pd.read_csv(file_path)
print("DataFrame originale:")
print(df)

print("-" * 150)

# 2) Mostro le prime 5 righe per avere un'anteprima
print("Prime 5 righe")
print(df.head())

print("-" * 150)

# 3) Mostro le ultime 5 righe per vedere la coda del dataset
print("Ultime 5 righe")
print(df.tail())

print("-" * 150)

# 4) Controllo i tipi di dati di ogni colonna (numerico, stringa, ecc.)
print("Tipo di dati di ciascuna colonna")
print(df.dtypes)

print("-" * 60)

# 5) Calcolo le medie di alcune colonne numeriche (Survived e Age)
print("Media")
media_surv = df['Survived'].mean()
media_age = df['Age'].mean()
print(media_surv)
print(media_age)

print("-" * 60)

# 6) Calcolo le mediane
print("Mediana")
mediana_surv = df['Survived'].median()
mediana_age = df['Age'].median()
print(mediana_surv)
print(mediana_age)

print("_" * 60)

# 7) Calcolo le deviazioni standard (variabilità dei dati)
print("Deviazione standard")
std_surv = df['Survived'].std()
std_age = df['Age'].std()
print(std_surv)
print(std_age)

print("_" * 60)

# 8) Rimuovo eventuali righe duplicate
df = df.drop_duplicates()


# 9) Gestione dei valori mancanti
#   - Età: riempio i NaN con la media dell'età
df['Age'] = df['Age'].fillna(df['Age'].mean())
#   - Survived: nel train.csv non ci sono NaN, ma se ci fossero li riempirei con la media
df['Survived'] = df['Survived'].fillna(df['Survived'].mean())

# 10) Aggiunta nuova colonna chiamata Categoria età
#   - 'Giovane': True se l'età è <= 18
#   - 'Adulto': True se l'età è <= 65
#   - 'Senior': True se l'età è > 65
df['Giovane'] = df['Age'] <= 18
df['Adulto'] = df['Age'] <= 65
df['Senior'] = df['Age'] > 65

print("\nDataFrame con colonna 'Giovane', 'Adulto' o 'Senior' in base all'età:")
print(df)

# 11) Salvo il DataFrame pulito in un nuovo file CSV
df.to_csv('titanic_pulito.csv', index=False)
