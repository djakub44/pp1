def f(uid):
    dict = {}
    for i in range(len(uid)):
        if uid[i] in dict.keys():
            return False
        else:
            dict[uid[i]] = 1
    return True


        



if __name__ == "__main__":

    print(f(["john5","ann123","JOHN5","xxx","abc333","a10"]))
    print(f(["abc123","ann","abc123","a10"]))
    print(f(["bob2","bob2"]))
    print(f(["bob2","BOB2"]))
