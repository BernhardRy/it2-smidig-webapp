# Navn på app

DrinksNGames.no

# Kort beskrivelse av appen

DrinksNGames.no er et spill hvor brukeren gjetter hvilke ingredienser en drink inneholder. 
For hver gang du velger riktig drink får du et poeng.

- [Prosjektbeskrivelse](./prosjektbeskrivelse.md)

## Skal gjøres

- [ ] Hva er planen din?
- [x] (drink_program.py) Hente og lese drink data fra api: https://www.thecocktaildb.com/api/json/v1/1/random.php
- [ ] Lage en klasse med funksjonene: Hent_drinker, hent_json_drinker, hent_ingredienser_til_drink og hent_riktig_drink

## Logg

### Uke 1

- Prøvde meg litt fram med ideer
- Funnet en katte api - du får tilfeldige katte bilder
- Begynt på et katte spill
- Idee: lage et spill hvor du velger en katt også skal du slåss mot en annen katt

### Uke 2

- Begynt på et poeng system til hver katt i en json fil
- Jobbet litt med html- og css filer

### Uke 3

- Jeg forkastet katte spill ideen
- Begynt på en finn.no copy - fant.no
- Laget en logo
- Jobber litt med hvordan jeg skal lage nettsiden
- Forkastet fant.no og begynt på et drink spill hvor man gjetter en drink basert på ingredienser

### Uke 4

- Laget et program som kjører gjennom en api som finner fire tilfeldige drinker 
- Laget funksjonene: hent_drinker, hent_ingredienser_til_drink, hent_riktig_drink og sjekk_vinn

### Uke 5

- Endret små ting i programmet
- Begynt litt på html filer til drink programmet

### Uke 6

- Laget kopling mellom drink programmet og html filene
- Fått inn de fleste variablene jeg trenger i app.py
- Sjekket at alt funker som det skal i index.html - det ser ut til å funke

### Uke 7

- Fikset slik at man får fire tilfeldige drinkers bilde og navn på nettsiden
- Fikset slik at ingrediensene til den riktige drinken synes på nettsiden
- Har prøvd meg litt på forms slik at man kan gjette på en drink - har ikke fått det til å funke ennå

### Uke 8

- Jeg har fikset forms i html filen slik at gjettet ditt lagres
- Jeg har fikset litt på index.html og style.css slik at nettsiden ser fin ut
- Jeg har lagt til et poengsystem slik at du får et poeng hver gang du får rett

## Tilbakemeldinger

- Fyll ut tilbakemeldinger her

## Hvordan kjøre web-appen

### Første gang

- Klon dette prosjektet med Github-deskop eller last det ned som .zip og pakk ut
- Kjør dette i terminalen: 
  - Mac: `python3 -m venv venv; . venv/bin/activate; pip install flask`
  - Windows: `py -3 -m venv venv && venv\\Scripts\\activate && pip install flask`
- Start prosjekt med å kjøre `app.py`, enten ved trykke play i `app.py` i VS Code eller skrive `python app.py`

### Ellers

- Aktiver virtuelt miljø i terminalen: 
  - Mac: `. venv/bin/activate`
  - Windows: `venv\\Scripts\\activate`
- Start prosjekt med å kjøre `app.py`, enten ved trykke play i `app.py` i VS Code eller skrive `python app.py`



