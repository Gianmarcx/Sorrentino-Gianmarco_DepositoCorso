#per la visualizzazione dei dati abbiamo delle librerie che ci aiutano , le quali SeaBorn e MatplotLib

#lo scopo è informativo ed esplorativo


#Esistono vari tipi di grafici:

#Dati Categorici
#Continui


#Matplotlib 

import matplotlib.pyplot as plt
import seaborn as sns 


#Seaborn lavora in tandem con Matplotlib , quindi molte delle impostazioni di stile di Seaborn influenzeranno i grafici creati con Matplotlib

#Matplotlibè altamente personalizzabile

plt.rcParams['figure.figsize'] = [10, 6]

# Imposta la dimensione predefinita delle figure


plt.rcParams['figure.dpi'] = 100



#Come creare un grafico seaborn e Matplotlib:

import matplotlib.pyplot as plt

import seaborn as sns

import numpy as np


# Configura Seaborn

sns.set_theme(style="darkgrid")


# Crea alcuni dati

data = np.random.normal(size=100)


# Crea un grafico

sns.histplot(data, kde=True)

plt.title('Distribuzione dei dati')

plt.show()

#Grafico  a Barre

import matplotlib.pyplot as plt

categories = ['A', 'B', 'C', 'D', 'E']

values = [3, 7, 2, 5, 8]


plt.figure()

plt.bar(categories, values)

plt.title('Grafico a Barre')

plt.xlabel('Categorie')

plt.ylabel('Valori')

plt.show()