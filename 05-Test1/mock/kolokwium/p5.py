def f(t,c,n):
    Counter = 0
    for x in t:
        if x == c:
            Counter+=1
    if Counter == n:
        return True
    else:
        return False



if __name__ == "__main__":
    print(f("abc","b",1))
    print(f("xxaxxbxx","x",6))
    print(f("qwerty","b",0))
    print(f("abcdef","b",2))
    print(f("book","o",1))
