import requests
import random

class Drinks:
    def __init__(self) -> None:
        self._drinker_usortert = []
        self._drinker_sortert = []
        self._ingredienser = []
        self._drinker_sortert_dic = {}
        self._bilder_og_ingredienser = []
        for i in range(4):
            link = "https://www.thecocktaildb.com/api/json/v1/1/random.php"
            o = requests.get(link)
            self._drinker_usortert.append(o.json())
        for i in self._drinker_usortert:
            self._drinker_sortert.append(i["drinks"][0]["strDrink"])
            self._bilder.append(i["drinks"][0]["strDrinkThumb"])
            midlertidig_ingredienser_drink = []
            for a in range(15):
                a += 1
                if not i["drinks"][0]["strIngredient"+str(a)] == None:
                        midlertidig_ingredienser_drink.append(i["drinks"][0]["strIngredient"+str(a)])
            self._drinker_sortert_dic[i["drinks"][0]["strDrink"]] = midlertidig_ingredienser_drink
            self._ingredienser.append(midlertidig_ingredienser_drink)

    def hent_drinker(self):
        return list(self._drinker_sortert_dic)
    
    def hent_bilder(self):
        return self._bilder
    
    def hent_ingredienser_til_drink(self):
        global randomtall
        global drinkListe
        drinkListe = list(self._drinker_sortert_dic.keys())
        randomtall = random.randint(0, len(drinkListe) - 1)
        randomDrink = drinkListe[randomtall]
        return self._drinker_sortert_dic[randomDrink]
    
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

drinker_usortert = []
drinker_sortert = []
ingredienser = []
drinker_sortert_dic = {}
bilder = []
for i in range(4):
    link = "https://www.thecocktaildb.com/api/json/v1/1/random.php"
    o = requests.get(link)
    drinker_usortert.append(o.json())
for i in drinker_usortert:
    drinker_sortert.append(i["drinks"][0]["strDrink"])
    bilder.append(i["drinks"][0]["strDrinkThumb"])
    midlertidig_ingredienser_drink = []
    for a in range(15):
        a += 1
        if not i["drinks"][0]["strIngredient"+str(a)] == None:
                midlertidig_ingredienser_drink.append(i["drinks"][0]["strIngredient"+str(a)])
    drinker_sortert_dic[i["drinks"][0]["strDrink"]] = midlertidig_ingredienser_drink
    ingredienser.append(midlertidig_ingredienser_drink)

print(drinker_sortert_dic)
                        