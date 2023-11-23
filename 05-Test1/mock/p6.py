import math

def f(number,even):
    result = 0
    strTemp = str(number)
    arr = [0]*len(strTemp)
    for i in range(0,len(strTemp)):
        arr[i]=int(strTemp[i])

        if even and arr[i] % 2 == 0:
            result+=arr[i]
        elif not even and arr[i] % 2 == 1:
            result+=arr[i]
    return result

        
        




if __name__ == "__main__":
    print(f(1234,True))
    print(f(3124,False))
    print(f(20576,False))
    print(f(20576,True))
    print(f(13115,True))