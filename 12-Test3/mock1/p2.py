def f (x,y,digit):
    counter = 0
    strD = str(digit)
    for i in range(x,y+1):
        for j in range(len(str(i))):
            if str(i)[j] == strD:
                counter+=1
    return counter


if __name__ == "__main__":
    print(f(10,15,1))
    print(f(28,32,2))
    print(f(100,105,6))
    print(f(100,101,0))