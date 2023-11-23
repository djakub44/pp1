def f(n1,n2,n3):
    if n1 == n2:
        return False
    else:
        if n1 == n3:
            return False
        else:
            if n2 == n3:
                return False
            else:
                return True
            
if __name__ == "__main__":
    print(f(1,2,3))
    print(f(1,1,3))
