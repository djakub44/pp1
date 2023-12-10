import json

movie = {
    "title":"Shrek",
    "year":"2000Iguess",
    "director":"Idontknow",
    "starring":{"main":"Eddie Murphy","supporting":"Idontknow"},
    "rating":10
}

with open("myMovie.json","w") as file:
    json.dump(movie,file,indent=6)