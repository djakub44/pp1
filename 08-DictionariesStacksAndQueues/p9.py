countries = [
    {"name" : "Poland", "population" : 37000000},
    {"name" : "Czech Republic", "population" : 5000000},
    {"name" : "Indonesia", "population" : 23456787654},
    {"name" : "Germany", "population" : 2345678},
    {"name" : "Vatican", "population" : 1}
]

print ("Country Population")
i = 0
while i < len(countries):
    print (f'{countries[i]["name"]} {countries[i]["population"]}')
    i += 1