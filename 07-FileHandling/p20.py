with open ("allproducts.txt","w") as destfile:
    with open("MeatAndFish.txt","r") as Source1:
        with open("GrainsAndBread.txt","r") as Source2:
            for line in Source1:
                destfile.write(line)
            for line in Source2:
                destfile.write(line)


