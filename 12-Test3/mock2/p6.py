def f(mnumbers):
    counter = 0
    arr=[]
    for i in range(1,8):
        arr.append(str(i))
    for c in "abcdABCD":
        arr.append(c)

    for n in mnumbers:
        for i in range(len(n)):
            if i == 0 and not (n[i] in arr or n[i] == "+" or n[i] == "-"):
                break    
            if i != 0 and n[i] not in arr:
                break
        else:
            counter+=1
    return counter
                
                       
            


if __name__ == "__main__":
    print(f(["A15","-31","7abC","+D1","-gH"]))
    print(f(["A05","-3+1","7ab8C","+D1","-22k"]))