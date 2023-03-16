import requests
import random

drinker_usortert = []
drinker_sortert = []
ingredienser = []
drinker_sortert_dic = {}
for i in range(4):
    link = "https://www.thecocktaildb.com/api/json/v1/1/random.php"
    o = requests.get(link)
    drinker_usortert.append(o.json())
for i in drinker_usortert:
    drinker_sortert.append(i["drinks"][0]["strDrink"])
    midlertidig_ingredienser_drink = []
    for a in range(15):
        a += 1
        if not i["drinks"][0]["strIngredient"+str(a)] == None:
                midlertidig_ingredienser_drink.append(i["drinks"][0]["strIngredient"+str(a)])
    drinker_sortert_dic[i["drinks"][0]["strDrink"]] = midlertidig_ingredienser_drink
    ingredienser.append(midlertidig_ingredienser_drink)

def hent_drinker():
    return list(drinker_sortert_dic)

def hent_ingredienser_til_drink():
    global randomtall
    global drinkListe

    drinkListe = list(drinker_sortert_dic.keys())
    randomtall = random.randint(0, len(drinkListe) - 1)
    randomDrink = drinkListe[randomtall]

    return drinker_sortert_dic[randomDrink]

def hent_riktig_drink():
    global randomtall
    global drinkListe

    return drinkListe[randomtall]

def sjekk_vinn():
    alle_drinker = hent_drinker()
    print(alle_drinker)
    gjett_drink = input(f"Hvilken drink tror du bruker ingrediensene {hent_ingredienser_til_drink()}?\n")
    if alle_drinker[int(gjett_drink)] == hent_riktig_drink():
        print(f"Riktig svar!")
        print(hent_riktig_drink())
    else:
        print(f"Feil svar, det var {hent_riktig_drink()}")

# print(hent_ingredienser_til_drink())
print(sjekk_vinn())