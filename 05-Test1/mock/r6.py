def f(t,c,n):
    if len(t)>0:
        intCounter = 0
        for i in range(0,len(t)):
            if c == t[i]:
                intCounter += 1
        if intCounter == n:
            return True
    return False

if __name__ == "__main__":

    print(f("daniel","r",0))
