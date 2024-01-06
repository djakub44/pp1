def f(word):
    if len(word) == 0:
        return ""
    strT = ""
    strR = word.lower()
    for i in range(len(strR)):
        for j in range(len(strR)):
            if j == i: 
                strT= strT + strR[j].capitalize()
            else:
                strT += strR[j]
        if i < len(strR)-1:
            strT += "-"
    
    return strT
    
if __name__ == "__main__":
    print(f("booK"))
    print(f("ok"))