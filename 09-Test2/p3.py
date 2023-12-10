def f(array2D):
    sumr = []
    sumc = []
    for i in range(len(array2D)):
        sumr.append(0)
        for j in range(len(array2D[i])):
            sumc.append(0)
            sumr[i] += array2D[i][j]
    for i in range(len(array2D)):
        for j in range(len(array2D[i])):
            sumc[j] += array2D[i][j]
   
    for k in range(len(sumr)):
        if sumr[k] !=  sumc[k]:
            return False
    return True





if __name__ == "__main__":
    print(f([[3,7,2],[4,2,5],[5,2,1]]))
    print(f([[3,7,2],[4,2,5],[9,2,1]]))