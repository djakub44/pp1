import json
import csv


dict = {}
with open("products.csv","r") as source:
    source_content = source.read()
dest_content = []
dest_line = {}
counter = 1
for line in source_content.splitlines():
    line_content = line.split(",")
    if counter == 1:
        headers = line_content
        for i in range(len(line_content)):
            dest_line[line_content[i]] = ""
    else:
        for i in range(len(line_content)):
            dest_line[headers[i]] = line_content[i]
    counter += 1
    dest_content.append(dest_line)

with open("products.json","w") as dest:
    json.dump(dest_content,dest,indent=6)