import requests
import random

class Drinks:
    def __init__(self) -> None:
        self._drinker_usortert = []
        self._drinker_sortert = []
        self._ingredienser = []
        self._drinker_sortert_dic = {}
        for i in range(4):
            link = "https://www.thecocktaildb.com/api/json/v1/1/random.php"
            o = requests.get(link)
            self._drinker_usortert.append(o.json())
        for i in self._drinker_usortert:
            self._drinker_sortert.append(i["drinks"][0]["strDrink"])
            bilder_og_ingredienser = []
            midlertidig_ingredienser_drink = []
            bilder = []
            bilder.append(i["drinks"][0]["strDrinkThumb"])
            for a in range(15):
                a += 1
                if not i["drinks"][0]["strIngredient"+str(a)] == None:
                        midlertidig_ingredienser_drink.append(i["drinks"][0]["strIngredient"+str(a)])
            bilder_og_ingredienser.append(midlertidig_ingredienser_drink)
            bilder_og_ingredienser.append(bilder)
            self._drinker_sortert_dic[i["drinks"][0]["strDrink"]] = bilder_og_ingredienser

    def hent_drinker(self):
        return list(self._drinker_sortert_dic)
    
    def hent_json_drinker(self):
        return self._drinker_sortert_dic
    
    def hent_ingredienser_til_drink(self):
        global randomtall
        global drinkListe
        drinkListe = list(self._drinker_sortert_dic.keys())
        randomtall = random.randint(0, len(drinkListe) - 1)
        randomDrink = drinkListe[randomtall]
        return self._drinker_sortert_dic[randomDrink][0]
    
    def hent_riktig_drink(self):
        global randomtall
        global drinkListe
        return drinkListe[randomtall]
    
    def sjekk_vinn(self):
        self.alle_drinker = self.hent_drinker()
        print(self.alle_drinker)
        self.gjett_drink = input(f"Hvilken drink tror du bruker ingrediensene {self.hent_ingredienser_til_drink()}?\n")
        if self.alle_drinker[int(self.gjett_drink)] == self.hent_riktig_drink():
            print(self.hent_riktig_drink())
        else:
            print(f"Feil svar, det var {self.hent_riktig_drink()}")

# print(hent_ingredienser_til_drink())

# drinker_usortert = []
# drinker_sortert = []
# ingredienser = []
# drinker_sortert_dic = {}
# for i in range(4):
#     link = "https://www.thecocktaildb.com/api/json/v1/1/random.php"
#     o = requests.get(link)
#     drinker_usortert.append(o.json())
# for i in drinker_usortert:
#     drinker_sortert.append(i["drinks"][0]["strDrink"])
#     bilder_og_ingredienser = []
#     midlertidig_ingredienser_drink = []
#     bilder = []
#     bilder.append(i["drinks"][0]["strDrinkThumb"])
#     for a in range(15):
#         a += 1
#         if not i["drinks"][0]["strIngredient"+str(a)] == None:
#                 midlertidig_ingredienser_drink.append(i["drinks"][0]["strIngredient"+str(a)])
#     bilder_og_ingredienser.append(midlertidig_ingredienser_drink)
#     bilder_og_ingredienser.append(bilder)
#     drinker_sortert_dic[i["drinks"][0]["strDrink"]] = bilder_og_ingredienser

# print(drinker_sortert_dic)

                        