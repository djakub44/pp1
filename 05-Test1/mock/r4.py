def f(w):
    result = ''
    if len(w)>0:
        result=w[0]
        blnPlus = True
        for i in range(1,len(w)):
            if blnPlus:
                result += "+"
                blnPlus = False
            else:
                result += "-"
                blnPlus = True
            result += w[i]
        return result
    else:
        return result
    
if __name__ == "__main__":
    print(f('daniel'))   
    print(f('xyz'))
    print(f('x'))
    print(f(''))