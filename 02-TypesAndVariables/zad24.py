#zad 24

strRegNumber = input("enter vechicle reg number: ")

print(strRegNumber)
print(strRegNumber[0])
if strRegNumber[0]+strRegNumber[1] == "KR" or strRegNumber[0]+strRegNumber[1] == "KK": #mozna dopisac male litery, oraz sprawdzenie czy sa minimum dwa znaki
    blnKrk = True
else:
    blnKrk = False
print(f'from Krakow: {blnKrk}')