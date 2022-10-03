""" Opdracht 1
1) Leg uit waarom de code in deze opdracht een foutmelding geeft:
   Je kent de locatie van de kar niet, je probeert die te overschrijven.

2) Los het probleem op. 
   De code moet alle boodschappen op de lijst overlopen.
   Vervolgens print het hoeveel er van iedere boodschap in de kar aanwezig is.
   Je mag de variabelen boodschappenlijst en kar niet aanpassen!
"""

boodschappenlijst = [
    "boter", "kaas", "spek", "bananen", "druiven", "aardappelen"
]

kar = {
    "boter": "1 vloot",
    "kaas": "200g",
    "bananen": "2 trossen",
    "aardappelen": "500g"
}

for boodschap in boodschappenlijst:
    if boodschap in kar:
        print(f"Er ligt {kar[boodschap]} {boodschap} in de kar.")
    else:
        print(f"Er is geen aanwezig")


    if boodschap in kar:
        print(f"Er ligt {kar.get(boodschap, 0)} {boodschap} in de kar.")        