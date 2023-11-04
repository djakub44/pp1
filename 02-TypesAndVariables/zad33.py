strPsw = input('enter password ')

if len(strPsw) >=8:
    blnPswValid = True
else:
    blnPswValid = False

print(f'valid? {blnPswValid}')
