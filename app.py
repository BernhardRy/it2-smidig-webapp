from flask import Flask, render_template, request
from drink_program import hent_drinker
import json

app = Flask(__name__)

@app.route("/")
def index():
    navn = "Sandvika"
    return render_template("index.html", navn=navn)

app.run(debug=True)