file = open('countries.txt','r')

counter = 0

for line in file:
    counter += 1
    print(f'{counter} {line}', end="")

file.close()

