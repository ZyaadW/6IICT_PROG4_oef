""" Oefening 4 (  / 2)
Maak onderstaande opdrachten over dictionaries.

Vergeet niet bij iedere regel code commentaar te schrijven.
"""

""" Opdracht 1:
Zoek in onderstaande dictionary de club die het MEESTE kaarten heeft ontvangen.
Print deze club. Opgelet! Dit programma moet ook blijven werken als de dictionary wijzigt.

RESULTAAT: Nederland
"""
aantal_kaarten_wk = {"Duitsland": 14, "Nederland": 24, "Spanje": 7, "Polen": 20}
for key,value in aantal_kaarten_wk.items():
    if max(aantal_kaarten_wk) == True:
        print(value)




# maximaal = max(aantal_kaarten_wk.values()) # Bereken de min/max WAARDE van de vermogens.
# aantal_kaarten_wk["max_verm"] = maximaal # Voeg maximale waarde toe aan dict info.
# for key in aantal_kaarten_wk:
#     if maximaal == key:
#         print(key)
""" Opdracht 2:
Print de waarde bij de key "corners".
"""
wk = {"Duitsland": {"status": "uitgeschakeld", "matchen_gespeeld": 3, "statistieken": {"kaarten": 14, "corners": 9.8, "CS%": 10}}}

print(wk["Duitsland"]["statistieken"]["corners"]) # ga in de dict "wk" en volg het pad 
""" Opdracht 3:
Vraag de gebruiker om een letter. Verwijder vervolgens alle keys waarin deze letter staat.
    Tip: gebruik if ... in ... om te controleren of een bepaalde letter in de key voorkomt.

Print de gewijzigde dictionary. 
Opgelet! Het programma mag geen onderscheid maken tussen kleine en grote letters.

VOORBEELD:
    Geef een letter op: L
    {"Spanje": 7}

    Geef een letter op: N
    {}

    Geef een letter op: z
    {"Duitsland": 14, "Nederland": 24, "Spanje": 7, "Polen": 20}

"""
aantal_kaarten_wk = {"Duitsland": 14, "Nederland": 24, "Spanje": 7, "Polen": 20}

gekozen_letter = input("Kies een letter: ")
dict2 = {}
for key,value in aantal_kaarten_wk.items():
    if key.count in gekozen_letter == 1:
        print(dict2)