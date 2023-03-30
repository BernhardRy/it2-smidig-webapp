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
    bilder = drinks.hent_bilder()

    return render_template("index.html", alle_drinker=alle_drinker, riktig_drink=riktig_drink, hent_ingredienser=hent_ingredienser, bilder=bilder)

@app.route('/handle_data', methods=['POST'])
def handle_data():
    projectpath = request.form['projectFilepath']
    return render_template("index.html", projectpath=projectpath)

app.run(debug=True)