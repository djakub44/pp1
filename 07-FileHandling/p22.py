import random as r

file = open("22.txt","w")

for i in range(1,51):
    file.write(str(r.randint(199,999)))
    file.write("\n")
file.close()
