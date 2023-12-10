import json

with open("students.json","r") as file:
    file_content = json.load(file)

print(file_content[0])
for i in file_content:
    i.pop("gender")
    i.pop("email")
    i.pop("age")
    i.pop("year")

with open("limited.json","w") as file2:
    json.dump(file_content,file2, indent=6)



