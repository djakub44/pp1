def f(arr):
    dict = {}
    for i in range(len(arr)):
        if arr[i] in dict.keys():
            dict[arr[i]] = dict[arr[i]]+1
        else:
            dict[arr[i]] = 1

    for key in dict:
        if dict[key] == 1:
            return key



if __name__ == "__main__":
    print(f([7,7,7,7,7,5,7,7]))