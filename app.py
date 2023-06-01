from flask import Flask, render_template, request, redirect
from drink_program import Drinks
import json

app = Flask(__name__)
riktig_drink = ""
poeng = 0
fasit = ""
ditt_gjett = ""

@app.route("/")
def index():
    global riktig_drink
    global poeng
    global fasit
    global ditt_gjett

    drinks = Drinks()
    alle_drinker = drinks.hent_drinker()
    hent_ingredienser = drinks.hent_ingredienser_til_drink()
    riktig_drink = drinks.hent_riktig_drink()
    hent_json = drinks.hent_json_drinker()
    print(poeng)

    return render_template("index.html", alle_drinker=alle_drinker, riktig_drink=riktig_drink, hent_ingredienser=hent_ingredienser, hent_json=hent_json, poeng=poeng, fasit=fasit, ditt_gjett=ditt_gjett)

@app.route("/gjett/<id>")
def func(id):
    global riktig_drink
    global poeng
    global fasit
    global ditt_gjett

    print(id)
    if id == riktig_drink:
        poeng += 1
        fasit = riktig_drink
        ditt_gjett = ""
    else:
        fasit = riktig_drink
        ditt_gjett = id
        
    return redirect("/")

app.run(debug=True,port=5001)