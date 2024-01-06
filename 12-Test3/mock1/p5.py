class C():
    def __init__(self,value):
        self.value = value 
        
    def __str__(self):
        return str(self.value)
    
    def m1(self):
        return self.value
    
    def m2(self):
        self.value += 1
    
    def m3(self):
        self.value = self.value - 1
    
    def m4(self,n):
        self.value = self.value + n

    def __add__(self,next):
        return self.value + next.value

if __name__ == "__main__":
    c=C(5)
    print(c.m1())
    c.m2()
    print(c.m1())
    c.m4(-8)
    print(c.m1())
    c.m3()
    print(c.m1())
    c.m4(10)
    print(c.m1())
    c.__str__()

    c2 = C(3)
    print(c+c2)