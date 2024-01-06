def f(fnc,prods):
    
    strR = ""

    for i in range(len(prods)):
        strR += fnc(prods[i])
        if i < len(prods)-1:
            strR += ","
    return strR


if __name__ == "__main__":

    prods = ["water","cheese","tomato"] 
    fnc1 = lambda x: "id:"+x[:2] 
    fnc2 = lambda x: (x[0]+x[-1]).upper() 

    print(f(fnc1,prods))
    print(f(fnc2,prods))