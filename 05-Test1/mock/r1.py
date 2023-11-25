
def f(a,b):
    if a>b:
        result = "".join((str(a), '-', str(b), '=', str(a-b)))
    else:
        result = "".join((str(a), '+', str(b), '=', str(a+b)))
    return result

if __name__ == "__main__":
    print (f(20,8))
    print (f(8,12))
