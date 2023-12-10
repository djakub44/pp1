import json
import requests

Req = requests.get ("http://api.nbp.pl/api/exchangerates/rates/C/eur/last/10?format=JSON")
print(Req.status_code)

with open("eur.json","w") as file:
    json.dump(Req.json(),file,indent=6)

with open("eur.json","r") as Source:
    with open("displayEUR.txt","w") as Dest:
        with open("displayEURCSV.csv","w") as DestCSV:
            eur_content = json.load(Source)

            Dest.write("date          bid rate      ask rate\n")
            DestCSV.write("date,bid_rate,ask_rate\n")
            Dest.write("====================================\n")
            
            #create txt user friendly and CSV
            for i in range(len(eur_content["rates"])):
                Dest.write(eur_content["rates"][i]["effectiveDate"])
                DestCSV.write(eur_content["rates"][i]["effectiveDate"])
                Dest.write('    ')
                DestCSV.write(',')
                Dest.write(str(eur_content["rates"][i]["bid"]))
                DestCSV.write(str(eur_content["rates"][i]["bid"]))
                Dest.write('        ')
                DestCSV.write(',')
                Dest.write(str(eur_content["rates"][i]["ask"]))
                DestCSV.write(str(eur_content["rates"][i]["ask"]))
                Dest.write("\n")
                DestCSV.write("\n")