file = open('shoppinglist.txt','a')

read_product = True

while read_product:
    product = input('what to buy? ')
    if product == "":
        read_product = False
    else:
        file.write(product+'\n')
    
file.close()
file = open('shoppinglist.txt','r')
file_content = file.read()
file.close()
print(file_content,end="")