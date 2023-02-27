import requests
import json

def hent_katte_bilde():
    katteListe = []
    # link = "https://api.thecatapi.com/v1/images/search?limit=1"
    # o = requests.get(link)
    fil = open("katte_poeng.json")
    a = json.load(fil)
    fil.close()
    
    for i in a["katter"]:
        katteListe.append(a["katter"][i])

    return katteListe

# def write_json(new_data, filename='katte_poeng.json'):
#     with open(filename,'r+') as fil:
#         fil_data = json.load(fil)
#         fil_data["katter"].append(new_data)
#         fil.seek(0)
#         json.dump(fil_data, fil, indent = 4)

# for i in range(5):
#     for a in hent_katte_bilde():
#         dictionary = {}
#         dictionary[] = {
#             "bilde": a,
#             "poeng": 0
#         }
#     write_json(dictionary)