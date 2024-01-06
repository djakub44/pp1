def f(vname):
    if len(vname) < 1 or len(vname) > 5:
        return False
    elif not(vname[0].isalpha() or vname[0] == "_"):
        return False
    else:
        for i in range(1,len(vname)):
            if not(vname[i].isdigit() or vname[i].isalpha() or vname[i] == "_"):
                return False
    return True


if __name__ == "__main__":
    print(f("abc"))
    print(f("Abc"))
    print(f("aBC"))
    print(f("_ab_c"))
    print(f("abcdef"))
    print(f("8abc"))
    print(f("_aB8_"))
    print(f("_4x"))