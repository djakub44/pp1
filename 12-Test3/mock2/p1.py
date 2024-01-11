def f(n):
    arr = []
    arr2 = []
    for d in str(n):
        arr.append(int(d))
    for i in range(len(arr)):
        if arr[i] % 2 == 1:
            arr2.append(arr[i])
    
    if len(arr2) == 0:
        return -1
    else:
        arr2.sort()
        return arr2[-1]-arr2[0]
        


if __name__ == "__main__":
    print(f(10852))
    print(f(7235973))
    print(f(4388) )
    print(f(846206) )
