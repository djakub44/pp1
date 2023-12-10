alfabetDict = {}

with open("nato.txt","r") as file:
    for line in file:
        alfabetDict[line[0]] = line.strip()

with open("ICAO.txt","w") as file2:
    for key in alfabetDict:
        file2.write(key + ' ' + alfabetDict[key] + '\n')
