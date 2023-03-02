from flask import Flask, render_template, request
from r import hent_katte_bilde
import json

app = Flask(__name__)

# bruker = ""

# fil = open("brukere.json")
# brukere = json.load(fil)
# fil.close()

@app.route("/")
def index():
    navn = "Sandvika"
    return render_template("index.html", navn=navn)

@app.route("/katter")
def katter():
    tilfeldigKatt1 = hent_katte_bilde()
    return render_template("katter.html", tilfeldigKatt1=tilfeldigKatt1)

# @app.route("/registrer", methods=("POST", "GET"))
# def rute_registrer():
#     if request.methods == "POST":
#         brukernavn = request.form["brukernavn"]
#         passord = request.form["passord"]
#         navn = request.form["navn"]

#         if brukernavn == "" or passord == "" or navn == "":
#             melding = "Fill in all forms"
#             return render_template("registrer.html", melding=melding)
#         elif brukernavn == brukere:
#             melding = "The username is taken"
#             return render_template("registrer.html", melding=melding)
#         else:
#             if brukernavn not in brukere:
#                 brukere[brukernavn] = {
#                     "navn": navn,
#                     "passord": passord,
#                     "bank": 20,
#                     "kjopt": []
#                 }
#                 skriv_brukere()
#                 return rute_logg_inn()
#             else:
#                 melding = "This username is taken"
#                 return render_template("registrer.html", melding=melding)
#     return render_template("registrer.html")

app.run(debug=True)