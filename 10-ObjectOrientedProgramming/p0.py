class kabanosy:
    def __init__(self,brand,amount):
        self.brand = brand
        self.amount = amount
        self.isedible = True
    def __str__(self):
        return f"{self.brand} {self.amount}g"
    def __add__(self,U):
        if self.brand == U.brand:
            return self.amount + U.amount 
        else:
            raise Exception("Adding different brand kabanoses is not possible")
    def __mul__(self,m):
        return self.amount*m
    
if __name__ == "__main__":
    kTar = kabanosy("Tarczynski",140)
    print(kTar)
    kTar2 = kabanosy("Tarczynski",200)
    kTar3 = kabanosy("Krakowskie",200)
    print(kTar+kTar2)
    print(kTar*2)

    print(kTar.isedible)    
    kTar.isedible = True
