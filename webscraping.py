from bs4 import BeautifulSoup
import requests
import json

# fil = open("imdb_top250.json", encoding="utf-8")
# filmliste = json.load(fil)

url = "https://viaplay.no/filmer"

result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")

finnFilmSjanger = doc.find_all('div', class_="Carousel-container-6KRfU")
f = doc.find('div', id='content')

for i in finnFilmSjanger:
    span = i.find('span')
    for a in span:
        print(a)
        print()