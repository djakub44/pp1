def f(n):
    for x in range(5):
        if x == n:
            print("found it")
            break
    else:
        print("not found") 

if __name__ == "__main__":
    f(3)