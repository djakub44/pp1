with open ("1.txt","r") as file:
    counter = 0
    for line in file:
        NextOne = False
        print(line, end="")
        counter += 1

        if counter % 5 == 0:
            while NextOne == False:
                if input("press enter ") == "":
                    NextOne = True
        