def f(Pswd):
    blnValid = True
    i = 0
    if len(Pswd) > 5:    
        for c in Pswd:
            for j in range(i,len(Pswd)-1):
                if c == Pswd[j+1]:
                    return False
            i += 1
        return True
    else:
        return False


if __name__ == "__main__":
    print(f('daniel'))
    print(f('danielel'))
    print(f('danie'))
    print(f('123456'))
    
