# tipo int
# sono sia numeri positivi che negativi 

x = 5
y = -5

print(x , y)

#tipo float

x = 2.5
y = -1.5

print(x , y)

#stringhe

s = "Python"
print(s[0]) #output 'P'
print(s[2]) #output: 't'

#Puoi concatenare stringhe usando l'operatore +

saluto = "Ciao"
nome = "Alice"
messaggio = saluto + "" + nome
print(messaggio) #Output: 'Ciao Alice'

#metodi per lavorare e incorporare le stringhe

len()#ottenere la lunghezza
upper()#converte una stringa in maiuscolo
lower()#converte uan stringha in minuscolo
split()#divide una stringha in una lista di sottostringhe in base a un delimitatore
replace()#sostituisce parti di una stringa con un'altra

s = "Ciao, mondo!"
print(len(s))# Output:12
print(s.upper())

#Caratteri char

carattere= 'A'


#Booleani 

x = 5
y = 10
z= 7

print(x < y and y > z)#Output: true
print(x < y or z > y)#Output: true
print(not(x < y)) #Output: false

x = 5
y = 10

print(x == y) #false
print(x != y) #true
print(x < y) #true
