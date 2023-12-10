file = open("shoppinglist.txt","r")

for line in file:
    print(line, end = "")

file.close

with open("shoppinglist.txt","r") as file:
    for line in file:
        print(line)

