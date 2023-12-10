with open ("1.txt","r") as SourceFile:
    with open("Copy.txt","w") as DestFile:
        DestFile.write (SourceFile.read())
