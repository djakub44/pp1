def f(player1,player2):
    Points = {
        "A":10,
        "K":10,
        "Q":10,
        "J":10,
        "T":10,
        "9":9,
        "8":8,
        "7":7,
        "6":6,
        "5":5,
        "4":4,
        "3":3,
        "2":2,
        "1":1
    }
    p1 = 0
    p2 = 0
    for c in player1:
        p1 += Points[c]
    for c in player2:
        p2 += Points[c]
    if p1 > p2:
        return True
    else:
        return False

if __name__ == "__main__":
    print(f("AJ972","AQT72"))
    print(f("9532","K8"))
