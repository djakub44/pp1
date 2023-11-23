
def f(card_number):

    newnumber = ""
    for i in range(0,16):
        if i > 1 and i < 12:
            newnumber += card_number[i].replace(card_number[i], "*")
        else:
            newnumber += card_number[i]
    return newnumber
    
if __name__ == "__main__":
    print(f("5290312400019022"))
