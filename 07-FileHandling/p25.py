import re

with open("25.txt","r") as file:
    file_content = file.read()

temperatures = re.findall("..C",file_content)
print(temperatures)

avg = 0
for i in range(len(temperatures)):
    avg += int(temperatures[i][0] + temperatures[i][1])
avg = avg / (1+ len(temperatures))
print(avg) 