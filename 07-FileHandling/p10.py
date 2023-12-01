file = open('countries.txt','r')
file_content = file.read()
print(file_content, end="")
file.close()