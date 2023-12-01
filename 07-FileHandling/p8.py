file = open('countries.txt','r') #r - read w - write a - append
file_content = file.read()
print(file_content)
print(file.closed)
file.close()
print(file.closed)
