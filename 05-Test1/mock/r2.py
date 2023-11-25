import math

def f(n):
    PrimeCounter = 0
    i = 2
    while PrimeCounter < n:
        blnPrime = True
        for j in range(2,i):
            if i % j == 0:
                blnPrime = False
        if blnPrime == True:
            PrimeCounter += 1
            PrimeNumber = i
        i += 1
    return PrimeNumber

if __name__ == "__main__":
    print(f(8))
