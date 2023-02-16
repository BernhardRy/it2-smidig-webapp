from flask import Flask, render_template
from r import hent_katte_bilde

app = Flask(__name__)



@app.route("/")
def index():
    navn = "Sandvika"
    return render_template("index.html", navn=navn)

@app.route("/katter")
def katter():
    tilfeldigKatt1 = hent_katte_bilde()
    tilfeldigKatt2 = hent_katte_bilde()
    return render_template("katter.html", tilfeldigKatt1=tilfeldigKatt1, tilfeldigKatt2=tilfeldigKatt2)

app.run(debug=True)