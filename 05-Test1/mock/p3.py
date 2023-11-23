def f(name):
    strResult = ""
    for word in name.split():
        strResult += word[0]
    return strResult

if __name__ == "__main__":
    print(f("Ala ma kota"))
