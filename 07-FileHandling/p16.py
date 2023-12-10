path = input("dawaj plik ")

with open(path) as file:
    print(path)
    counter = 0
    for line in file:
        counter+= 1
    print (counter)

