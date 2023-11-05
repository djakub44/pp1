import mymath, mykeyboard

x = mykeyboard.read_number()
y = mymath.generate_number()

print(f'your number: {x}')
print(f'PC number: {y}')

if x == y:
    print('you won')
else:
    print('you lost')

    