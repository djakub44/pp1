def month(n):
    if n > 0 and n < 13:
        Months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
        return Months[n-1]
    else:
        return ""

if __name__ == "__main__":
    print(month(0))
    print(month(3))