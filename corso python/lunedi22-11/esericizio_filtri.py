def is_even(x):
    return x % 2 == 0

numbers = [1,2,3,4,5,6,7,8,9,10]

def somma(x):
    return numbers[x] + numbers[x + 1] > numbers[x + 2]

indici = range(len(numbers) - 2)
risultato =  list(filter(somma,indici))

print(risultato)