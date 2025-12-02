from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

data = load_iris() #carico dataset load_iris

X = data.data #caratteristiche
y = data.target #etichette

# Divisione dei dati in set di addestramento e di test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


#Creazione modello KNN con 5 vicini
model = KNeighborsClassifier(n_neighbors=5)
model.fit(X_train,y_train) #addestramento modello sui dati di training

predictions = model.predict(X_test) #predizione sul test set

accuracy = accuracy_score(y_test, predictions) #calcolo l'accuratezza confrontando predizioni e valori reali


#Stampa risultato finale
print(f'Accuracy finale: {accuracy:.2f}')
