def f(n):
    for x in range(5):
        if x == n:
            return "found it"
            break
    else:
        return "not found"

if __name__ == "__main__":
    result = f(3)
    x = 3
    myL = lambda s,i : s[i]

    y = myL(result,x)
    print(y)
