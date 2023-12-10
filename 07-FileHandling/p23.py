import math as m

with open("23.txt","w") as file:
    for i in range(1,11):
        file.write(str(i))
        file.write(",")
        file.write(str(int(m.pow(i,2))))
        file.write(",")
        file.write(str(int(m.pow(i,3))))
        file.write("\n")