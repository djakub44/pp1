import csv

with open("24.csv","r") as file:
    csvFile = csv.reader(file)
    for line in csvFile:
        if line[2] != "age":
            if int(line[2]) < 30:
                print(f'{line[0]} {line[1]} {line[4]}')
