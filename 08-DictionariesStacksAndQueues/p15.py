basic_data = {
    "name":"Barbara",
    "age":21
}

advanced_data = {
    "status":"student",
    "married":False,
    "interest":["reading","swimming"]
}

person = {}

for key in basic_data:
    person[key]=basic_data[key]

for key in advanced_data:
    person[key]=advanced_data[key]

for key in person:
    print(key)
    print(person[key])