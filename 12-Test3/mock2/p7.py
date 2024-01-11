def f(d):
    arrIn = []
    arrOut = []
    arrtmp = []
    for v in d:
        if v[1] == "in":
            arrIn.append(v[0])
            arrtmp.append(v[0])
        elif v[1] == "out":
            arrOut.append(v[0])
        else:
            return -1
    
    for v in arrtmp:
        if v in arrOut:
            arrIn.remove(v)
            arrOut.remove(v)
    arrIn.sort()
    return arrIn

if __name__ == "__main__":
    cars = [["KR234","in"],["BA123","in"],["GX444","in"],["KR234","out"], ["BA111","in"],["BA123","out"],["KR234","in"]]
    print(f(cars))
    cars1 = [["KR234","in"],["KR234","out"]]
    print(f(cars1))
