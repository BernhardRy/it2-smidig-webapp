from flask import Flask, render_template, request, redirect
from drink_program import Drinks
import json

app = Flask(__name__)

with open("high_score.json", "r") as fil:
    data = json.load(fil)

best_score = data["high_score"]


riktig_drink = ""
poeng = 0
fasit = ""
ditt_gjett = ""

@app.route("/")
def index():
    global riktig_drink, poeng, fasit, ditt_gjett, best_score


    drinks = Drinks()
    alle_drinker = drinks.hent_drinker()
    hent_ingredienser = drinks.hent_ingredienser_til_drink()
    riktig_drink = drinks.hent_riktig_drink()
    hent_json = drinks.hent_json_drinker()
    # print(poeng)
    print(best_score)

    return render_template("index.html", alle_drinker=alle_drinker, riktig_drink=riktig_drink, hent_ingredienser=hent_ingredienser, hent_json=hent_json, poeng=poeng, fasit=fasit, ditt_gjett=ditt_gjett, best_score=best_score)

@app.route("/gjett/<id>")
def func(id):
    global riktig_drink
    global poeng
    global fasit
    global ditt_gjett
    global best_score

    print(id)
    if id == riktig_drink:
        poeng += 1
        fasit = riktig_drink
        ditt_gjett = id
    else:
        if best_score < poeng:
            with open("high_score.json", "w") as fil:
                json.dump({"high_score": poeng}, fil)
                best_score = poeng

        fasit = riktig_drink
        ditt_gjett = id
        poeng = 0
        
    return redirect("/")

app.run(debug=True,port=5001)