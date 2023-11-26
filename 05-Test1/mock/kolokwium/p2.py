def f(n1,n2):
    for c1 in str(n1):
        for c2 in str(n2):
            if c1 == c2:
                return True
    else:
        return False 
    
if __name__ == "__main__":
    print(f(12,456))
    print(f(12,715))
    print(f(4455,90951))
    print(f(4455,777666555))