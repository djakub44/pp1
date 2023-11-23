def f(binary_number):
    for i in binary_number:
        if i != "0" and i != "1":
            return False
    return True




if __name__ == "__main__":
    print(f("101101"))
    print(f("1311a10100"))