name = "Daniel"
university = "UEK"
field = "Applied Informatics"

file = open('student.txt','w')
file.write(name+'\n')
file.write(university+'\n')
file.write(field+'\n')

file.close()


