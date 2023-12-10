import re

with open("28.txt","r") as file:
    file_content = file.read()

arr = re.findall("\S.....",file_content)
print(arr)