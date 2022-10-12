""" Opdracht 2: (  /3)
Maak een functie met...
 - Als argument een lijst van dictionaries: deze bevat info over acteurs (zie info_acteurs).
 - Als naam lengtes_acteurs.
 - Als return-waarde een lijst met erin de lengtes van de acteurs.

Opgelet! Niet iedere dictionary bevat de lengte van de acteur. 
         Als de dictionary geen lengte bevat voeg je "Niet Gegeven"
         toe aan de lijst.

 >>> lengtes_acteurs([{"name": "Q. Tarentino", "leeftijd": 59, "lengte": 170},
                      {"name": "S.L. Jackson", "leeftijd": 73}])
     [170, 'Niet Gegeven']

1 punt gaat op het correct aanmaken/oproepen van de functie.
2 punten op een juiste werking van deze functie.
"""

info_acteurs = [
    {"name": "Q. Tarentino", "leeftijd": 59, "lengte": 170},
    {"name": "J. Travolta", "leeftijd": 68, "lengte": 178},
    {"name": "S.L. Jackson", "leeftijd": 73},
    {"name": "U. Thurman", "leeftijd": 53, "lengte": 158}
]

def acteurs(info):
        lengtes_acteurs = []
        for acteurs in  info:
            if "lengte" in acteurs:    
                lengtes_acteurs.append(acteurs["lengte"])
            else:    
                lengtes_acteurs.append("Niet gegeven.")
        return(lengtes_acteurs)

print (acteurs(info_acteurs))        

