def f(b1,b2,b3,b4):
    Counter = 0
    if b1 == True:
        Counter+=1
    if b2 == True:
        Counter+=1
    if b3 == True:
        Counter+=1
    if b4 == True:
        Counter+=1
    if Counter > 2:
        return True
    else:
        return False


if __name__ == "__main__":
    print(f(True,False,True,True))
    print(f(False,False,True,True))
    print(f(True,True,True,True))
    print(f(True,False,False,False))