alfabetDict = {}

with open("nato.txt","r") as file:
    for line in file:
        alfabetDict[line[0]] = line.strip()

text = input("go ahead: ")

for c in text:
    print(alfabetDict[c.capitalize()], end=" ")
