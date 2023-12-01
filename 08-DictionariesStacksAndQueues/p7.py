person = {
    "name": "Marek",
    "surname": "Banach",
    "age": 25,
    "hobby": ["swimming","excursions"],
    "married": True,
    "phone":{"landline":"123444321","mobile":"777888999"}
   }

#a
for element in person:
    print(f'{element} : {person[element]}')

#b
print(person["name"])

#c
for i in person["hobby"]:
    print(i)

#d 
person["surname"] = "Nowak"

#e
person["married"] = not person["married"]

#f
person["gender"] = "male"
print(person["gender"])

#g
person["hobby"].append("bicycle")
# person["hobby"] = person["hobby"] + ["bicycle"] #dodawanie tablic
for i in person["hobby"]:
    print(i)

#h
person["phone"]["work phone"] = '313131444'
print(person["phone"])
