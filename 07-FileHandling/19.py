with open("1.txt","r") as sourcefile:
    with open("copylines.txt","w") as destfile:
        for line in sourcefile:
            destfile.write(line)