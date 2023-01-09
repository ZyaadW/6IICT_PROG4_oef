""" Oefening 1 (  / 2)
Maak onderstaande opdrachten over dictionaries.
Vergeet niet bij iedere regel code commentaar te schrijven.
"""

""" Opdracht 1:
Print voor IEDER element in onderstaande dictionary volgende tekst:
    <key> heb ik <value> uren per week

Voorbeeld:
    wisk heb ik 4 uren per week
    ...
    sph heb ik 2 uren per week
"""
vakken = {"wisk": 4, "prog": 4, "cosn": 2, "sph": 2} # dit is de dictionary met key en value

for key, value in vakken.items(): # hier wordt de dict ontleed naar 2 variabelen   
    print(f"{key} heb ik {value} uren per week") # print dit

""" Opdracht 2:
Vraag de gebruiker naar een vak. Print het aantal uur dat dit vak voorkomt in de dictionary.
Als het ingegeven vak niet bestaat, print dan "vak bestaat niet".

VOORBEELD:
    Geef een vak op: wisk
    4

    Geef een vak op: huppel
    vak bestaat niet
"""
vakken = {"wisk": 4, "prog": 4, "cosn": 2, "sph": 2}  # dit is de dictionary met key en value

keuze_dag = input("kies een vak: ") # kies een vak en stop in variabelen

for key,value in vakken.items(): #  hier wordt de dict ontleed naar 2 variabelen
    if keuze_dag == key:# als de keuze gelijk is aan de key
        print(f"{key}\n{value}") # print de key en value met een enter
        break # stop
    else: # anders
        print("Het vak bestaat niet") # print dit   
""" Opdracht 3:
Schrijf een programma dat onderstaande 2 lijsten combineert in een dictionary.
print deze dictionary. Opgelet! Dit programma moet ook blijven werken als de lijsten wijzigen.
                                De lijsten zullen wel altijd evenveel elementen bevatten.

RESULTAAT: {"wisk": 4, "prog": 4, "cosn": 2, "sph": 2}
"""
namen = ["wisk", "prog", "cosn", "sph"] # lijst namen
uren = [4,4,2,2] # lijst uren

dict = dict(zip(namen, uren)) # rits de namen en uren aan elkaar vast en plaats in dict
print(dict) # print dict



""" Opdracht 4:
Verander in onderstaande dictionary de key "error" naar "cosn". 
De volgorde van de dictionary hoeft niet hetzelfde te blijven. Print de dictionary. 

RESULTAAT: {"wisk": 4, "prog": 4, "cosn": 2, "sph": 2}
"""
vakken = {"wisk": 4, "prog": 4, "error": 2, "sph": 2} # dit is de dictionary met key en value

vakken["cosn"] = vakken.pop("error") # pas de dict aan 
print(vakken)  # print de vakken 
