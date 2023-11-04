
#zad 29
import random


intK1 = random.randint(1,6)
intK2 = random.randint(1,6)
intK3 = random.randint(1,6)

print(f'dice 1: {intK1}')
print(f'dice 2: {intK2}')
print(f'dice 3: {intK3}')
print(f'sum :{intK1 + intK2 + intK3}')

#zad30
print(f'dice 1: {intK1}')
if intK1 == 1 or intK1 == 6:
    blnSpecial = True
else:
    blnSpecial = False

print(f'special: {blnSpecial}')

#zad 31

intUserGuess = int(input('jaka liczba? '))
if intUserGuess == intK1:
    blnGuess = True
else:
    blnGuess = False

print(f'guessed? {blnGuess}')
