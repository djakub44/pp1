import math
import myModule

y = 10
print(type(y))

add_numbers = lambda a,b : a + b

numbers = [1,2,3]
result = map(lambda x: x+x,numbers)
print (list(result))

print(math.log(5))
print(math.pow(math.e, 5))
print(math.sin(math.pi/2))

#BMI
mass = 70
height = 180

BMI = lambda m,h:m/(math.pow(h,2))
print(BMI(mass,height))
print (myModule.f(1,2))