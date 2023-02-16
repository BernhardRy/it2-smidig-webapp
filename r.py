import requests
import json

def hent_katte_bilde():
    katteListe = []
    link = "https://api.thecatapi.com/v1/images/search?limit=1"
    o = requests.get(link)
    for i in o.json():
        katteListe.append(i['url'])

    return katteListe

for i in range(20):
    for a in hent_katte_bilde():
        dictionary = {}
        dictionary[i] = {
            "bilde": a,
            "poeng": 0
        }

        json_object = json.dumps(dictionary, indent=4)
        with open("katte_poeng.json", "w") as outfile:
            outfile.write(json_object)


