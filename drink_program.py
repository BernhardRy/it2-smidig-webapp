import requests
import random

class Drinks:
    def __init__(self) -> None:
        self._drinker_usortert = []
        self._drinker_sortert = []
        self._ingredienser = []
        self._drinker_sortert_dic = {}
        tall = 0

        def drinken():
            link = "https://www.thecocktaildb.com/api/json/v1/1/random.php"
            o = requests.get(link)
            en_drink = o.json()
            return en_drink
        
        while tall < 4:
            if drinken()["drinks"][0]["strAlcoholic"] != "Non Alcoholic":
                tall += 1
                self._drinker_usortert.append(drinken())
            else:
                print("hade")
            
        for i in self._drinker_usortert:
            # if i["drinks"][0]["strAlcoholic"] == "Alcoholic":
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