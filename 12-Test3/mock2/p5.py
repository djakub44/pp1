class C:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def m1(self):
        if self.x == 0 or self.y == 0:
            return 0
        else:
            if self.x * self.y > 0:
                if self.x > 0:
                    return 1
                else:
                    return 3
            else:
                if self.x > 0:
                    return 4
                else:
                    return 2
    def m2(self,a,b):
        tmp = C(a,b)
        if self.m1() == tmp.m1():
            return True
        else:
            return False

    def m3(self,a,b):
        power=-2
        if ((self.x-a)*(self.x-a) + (self.y-b)*(self.y-b)) > 25:
            return True
        else:
            return False
        


if __name__ == "__main__":
    p = C(2,3)
    print(p.m1())
    print(p.m2(7,4))
    print(p.m2(-3,1))
    print(p.m3(8,5))
    print(p.m3(4,7))
    p1 = C(0,5)
    print(p1.m1())
    print(p1.m2(4,7))
    print(p1.m2(-7,0))
