from flask import Flask, render_template, request
from drink_program import Drinks
import json

app = Flask(__name__)

@app.route("/")
def index():
    drinks = Drinks()
    alle_drinker = drinks.hent_drinker()
    hent_ingredienser = drinks.hent_ingredienser_til_drink()
    riktig_drink = drinks.hent_riktig_drink()
    hent_json = drinks.hent_json_drinker()

    return render_template("index.html", alle_drinker=alle_drinker, riktig_drink=riktig_drink, hent_ingredienser=hent_ingredienser, hent_json=hent_json)

app.run(debug=True)