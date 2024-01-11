def f(fnc,res):
    arr = []
    for score in res:
        if fnc(score):
            arr.append(score)
    
    if len(arr) == 0:
        return -1
    else:
        arr.sort()
        return arr[-1]-arr[0]

if __name__ == "__main__":
    res = [95,90,20,50,70] 
    fnc1 = lambda x: x>50
    print(f(fnc1,res))
    fnc2 = lambda x: x>30 and x<90
    print(f(fnc2,res))
