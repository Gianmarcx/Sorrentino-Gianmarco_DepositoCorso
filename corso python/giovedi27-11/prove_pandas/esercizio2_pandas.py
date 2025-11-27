import pandas as pd 
import numpy as np

#percorso del file csv
file_path = 'corso python/giovedi27-11/prove_pandas/dataset_vendite.csv'

#  Carico il dataset in un DataFrame
df = pd.read_csv(file_path)
print("DataFrame originale:")
print(df)

print("-" * 80)

#  Aggiungo la colonna "Totale Vendite", che è il risultato del prodotto tra Quantità e Prezzo Unitario
df['Totale Vendite'] = df['Quantità'] * df['Prezzo Unitario']
print(df)

print("-" * 80)


#  Trovo il prodotto più venduto in termini di pezzi:
#    - Raggruppo per Prodotto
#    - Sommo la Quantità per ogni prodotto
#    - Prendo il nome del prodotto con la somma più alta (idxmax) e il valore corrispondente (max)
print("PRODOTTO BEST SELLER")
best_seller = df.groupby('Prodotto')['Quantità'].sum().idxmax()
quantità_top = df.groupby('Prodotto')['Quantità'].sum().max()
print(f"{best_seller} ha venduto {quantità_top} pezzi")

print("-" * 80)

#  Trovo la città con il totale vendite più alto:
#    - Raggruppo per Città
#    - Sommo la colonna Totale Vendite
#    - Prendo la città con il totale più alto e il suo valore
print("CITTA CON PIU' VENDITE")
città_top = df.groupby('Città')['Totale Vendite'].sum().idxmax()
vendite_totali = df.groupby('Città')['Totale Vendite'].sum().max()
print(f"{città_top} ha {vendite_totali} vendite totali")

print("-" * 80)

#  Filtro solo le righe dove il Totale Vendite è maggiore di 2000
#    Creo un nuovo DataFrame con queste righe
print("DATAFRAME VENDITE TOTALI MAGGIORI A")
dataframe_vendite = df[df['Totale Vendite'] > 2000]
print(dataframe_vendite)

print("-" * 80)

 #Ordino il DataFrame originale dal più alto al più basso per Totale Vendite
print("DATA FRAME ORDINE DECRESENTE")
df_ordinato = df.sort_values(by='Totale Vendite', ascending=False)
print(df_ordinato)

#visualizzo il numero di vendite per ogni città.
vendite_città = df.groupby('Città')['Quantità'].sum()
print(vendite_città)