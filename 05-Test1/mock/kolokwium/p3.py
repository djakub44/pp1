def f(t):
    Result = ""
    for i in range(len(t)):
        for j in range(i+1):
            Result += t[i]
        if i != len(t)-1:
            Result+="-"
    return Result

if __name__ == "__main__":
    print(f("super"))
    print(f("ok"))
    print(f("a"))
    
