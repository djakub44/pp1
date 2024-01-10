def f(arr2D):
    arrSum = [0]*len(arr2D[0])
    for i in arr2D:
        for j in range(len(i)):
            arrSum[j]+=i[j]

    for i in range(len(arrSum)):
        for j in range(i+1, len(arrSum)):
            if arrSum[i] == arrSum[j]:
                return True
    else:
        return False

if __name__ == "__main__":
    #print(f([[3,4,2],[5,1,6]]))
    print(f([[3,4,2],[5,1,6]]))
    print(f([[3,4,2],[5,1,7]]))