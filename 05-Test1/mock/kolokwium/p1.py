def f(n):
    Fib1=0
    Fib2=1
    Fibn=0
    for i in range(2,n):
        Fibn = Fib1 + Fib2
        Fib1 = Fib2
        Fib2 = Fibn
    return Fibn


if __name__ == "__main__":
    print(f(5))
    print(f(9))
    print(f(11))