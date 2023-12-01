import json

with open("data.json") as file:
    data = json.load(file)

i = 0
for key,value in data.items():
    print(f'{key} {value}')
    if i > 10:
        break
    i +=1