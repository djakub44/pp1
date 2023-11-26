def f(n):
    if n < 1:
        return -1
    if n == 1:
        return 0
    if n == 2:
        return 1
    fib = f(n-1)+f(n-2)
    return fib

if __name__ == "__main__":
    print (f(1))
    print (f(2))
    print (f(3))
    print (f(4))
    print (f(5))
    print (f(19))