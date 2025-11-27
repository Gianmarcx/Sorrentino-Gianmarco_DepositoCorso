# Importiamo le librerie necessarie
import pandas as pd   # Pandas serve per lavorare con tabelle (DataFrame)
import numpy as np    # NumPy serve per generare dati casuali e fare calcoli numerici

# Impostiamo un seme per la generazione casuale
# In questo modo i risultati saranno sempre uguali ogni volta che esegui il codice
np.random.seed(42)

# Creiamo un intervallo di date dal 1 al 27 novembre 2025
data_range = pd.date_range(start='2025-11-01', end='2025-11-27')

# Definiamo le possibili città e prodotti
città = ['Napoli', 'Roma', 'Milano']
prodotti = ['Laptop', 'Smartphone', 'Tablet']

# Generiamo un dizionario con 20 righe di dati casuali
data = {
    'Data': np.random.choice(data_range, size=20),         # 20 date casuali
    'Città': np.random.choice(città, size=20),             # 20 città casuali
    'Prodotto': np.random.choice(prodotti, size=20),       # 20 prodotti casuali
    'Vendite': np.random.randint(100, 1000, size=20)       # 20 numeri casuali tra 100 e 999
}

# Creiamo un DataFrame Pandas a partire dal dizionario
df = pd.DataFrame(data)

# Salviamo il DataFrame in un file CSV
file_path = 'corso python/giovedi27-11/prove_pandas/vendite_fittizie.csv'
df.to_csv(file_path, index=False)   # index=False evita di salvare la colonna degli indici

# Ricarichiamo il dataset dal CSV (simuliamo di leggere un file esterno)
df = pd.read_csv(file_path)
print("DataFrame originale:")
print(df)

# Creiamo una tabella pivot:
# - index='Prodotto' → righe = prodotti
# - columns='Città' → colonne = città
# - values='Vendite' → valori = vendite
# - aggfunc='mean' → calcoliamo la media delle vendite
pivot_df = df.pivot_table(values='Vendite', index='Prodotto', columns='Città', aggfunc='mean')
print("\n--- Tabella Pivot (media vendite per prodotto e città) ---")
print(pivot_df)

# Usiamo groupby per sommare le vendite totali per ogni prodotto
grouped_df = df.groupby('Prodotto')['Vendite'].sum()
print("\n--- Vendite Totali per Prodotto ---")
print(grouped_df)
