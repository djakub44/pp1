file = open('numbers.txt','r')
sum = 0
strResult = "Numbers: "

for line in file:
    sum += int(line)
    strResult += line.strip()
    strResult += " "
print(strResult)
print(f'Sum: {sum}')

file.close()