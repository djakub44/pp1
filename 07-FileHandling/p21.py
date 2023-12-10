file = open("21.txt","w")

for i in range(1,51):
    file.write(str(i))
    file.write("\n")
file.close()