

# strDesc = input('enter description ')
personal_data = 'Mr. John May, born on 1998-02-16'

strDesc = personal_data.split()

print(f'name {strDesc[1]}')
print(f'Surname {strDesc[2][0:-1]}') #range from 0 to -1 to avoid comma
print(f'Initials {strDesc[1][0]+strDesc[2][0]}')
print(f'Born: {personal_data[-10:]}')