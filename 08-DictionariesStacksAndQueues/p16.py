def hotel_list(hotels):
    hl = []
    for i in range(len(hotels)):
        hl.append(hotels[i]["name"])
    return hl


def avg_price(hotels):
    sum = 0
    counter = 0
    for i in range(len(hotels)):
        sum += hotels[i]["price"]
        
    return (sum/len(hotels))
    

if __name__ == "__main__":

    Hotels_in_Krakow = [
        {"name":"Sky","price":320.00},
        {"name":"Metropol","price":480.00},
        {"name":"New Port","price":420.00},
        {"name":"Aparthotel","price":390.00}
    ]
    Hotels_in_Sopot = [
        {"name":"Focus","price":510.00},
        {"name":"Aqua","price":345.00},
        {"name":"La Boutique","price":390.00},
        {"name":"Marina","price":410.00}
    ]
    
    print(hotel_list(Hotels_in_Krakow))
    print(hotel_list(Hotels_in_Sopot))
    print(avg_price(Hotels_in_Krakow))
    print(avg_price(Hotels_in_Sopot))