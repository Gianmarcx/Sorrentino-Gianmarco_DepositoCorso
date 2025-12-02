#Per machine learing parliamo del campo di intelligenza artificiale (AI) che permette al pc di imparare dei dati e migliorare le proprie prestazioni senza essere esplicitamente programmati
#automatizza processi decisionali

#Nel contesto di machine learning un modello è un costrutto matematica che rappresenta la relazione tra input(dati) e output desiderati

#Il machine learing utilizza grandi quantità di dati per insegnare ai modelli di AI


#APPRENDIMENTO SUPERVISIONATO: il modello viene addestrato su set di dati che include sia input che gli output desiderati
#ha come obiettivo costruire un modello che possa fare previsioni accurate su nuovi dati basandosi su questa corrispondenza

#APPRENDIMENTO NON SUPERVISIONATO : Il modello lavora con dati che non hanno etichette
#l'obiettivo è scoprire strutture nascoste nei dati. Tecniche comuni includono il clustering

#APPRENDIMENTO PER RINFORZO: è una tecnica in cui un agente impara a prendere decisioni ottimzzando 

#OVERFITTIG: si verifica quando un modello impara bene i dettagli dei dati di addestramento, inclusi i rumori e le anomalie , a scapito delle prestrazioni sui nuovi dati

#UNDERFITTING: si verifica quando un modello è troppo semplice per catturare la struttura dei dati 



#VALIDAZIONE E TEST:

#Dopo l'addestramento i modelli vengono valutati su set di dati, 





#PRIMO MODELLO DI MACHINE LEARNING


# Importazione delle librerie necessarie

from sklearn.datasets import load_iris

from sklearn.model_selection import train_test_split

from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import accuracy_score


# Caricamento del dataset

data = load_iris()

X = data.data # le caratteristiche

y = data.target # le etichette


# Divisione dei dati in set di addestramento e di test

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# Creazione del modello di classificazione

model = RandomForestClassifier(n_estimators=100, random_state=42)


# Addestramento del modello

model.fit(X_train, y_train)


# Predizione delle etichette per il set di test

predictions = model.predict(X_test)


# Calcolo dell'accuratezza del modello

accuracy = accuracy_score(y_test, predictions)

print(f'Accuracy: {accuracy:.2f}')



