def f(a,b):
    result = ''
    if a < b:    
        for i in range(a,b+1):
            if i % 2 == 0:
                if result != '':
                    result+=','
                result += str(i)
    return result

if __name__ == "__main__":
    print (f(2,3))
    print (f(3,11))
    print (f(4,6))