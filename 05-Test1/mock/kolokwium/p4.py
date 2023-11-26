def f(n):
    Result = 0
    if n % 2 == 0:
        Result = n * (-1)
    else:
        if n > 0: 
            Result = n
        else:
            Result = n * (-1)
    return Result


if __name__ == "__main__":
    print(f(4))
    print(f(-4))
    print(f(5))
    print(f(-5))
