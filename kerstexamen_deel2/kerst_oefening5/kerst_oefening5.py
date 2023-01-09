""" Oefening 5 (  / 4)
Het JSON-bestand kerst_oefening5.json bevat een agenda.
Het zou echter handiger zijn als deze agenda in een CSV-bestand stond.

Lees kerst_oefening5.json in, in een Python variabele.
Schrijf deze vervolgens weg naar een bestand kerst_oefening5.csv.
kerst_voorbeeld5.csv toont hoe dit CSV-bestand er uit moet zien.

ALLES wat je naar dit CSV-bestand schrijft, moet uit het JSON-bestand komen. Manueel zaken ingeven mag dus niet.
Dit zodat het converteren blijft werken, ook wanneer je een andere JSON-agenda zou gebruiken.
Je mag ervanuit gaan dat iedere dag HETZELFDE aantal activiteiten heeft.
"""
import json,csv # importeer de modules

fp = open("kerstexamen_deel2/kerst_oefening5/kerst_oefening5.json")  # open json bestand via pad 
data = json.load(fp) # geef variabele de functie op het bestand in te laden
csv_lijst = [] # lege lijst

for rij in data: # voor rij in data
    csv_lijst.append(rij) # voeg rij toe aan lijst

fp1 = open("kerstexamen_deel2/kerst_oefening5/kerst_oefening5.csv", newline="") # open bestand volgens pad
writer = csv.DictWriter(fp1)  # laad in variabele

verwerkte_csv = [] # lege lijst
writer.writeheader() # schrijf header
for rij in verwerkte_csv : # voor rij in verwerkte csv
    writer.writerow(rij)

fp.close() # sluit bestand