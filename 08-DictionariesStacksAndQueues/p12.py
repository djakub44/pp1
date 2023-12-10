import json

dict = {
    "name":"daniel",
    "index":123,
    "somedata":"data"
}

with open ("studentdata.json","w") as file:
    json.dump(dict,file,indent=6)