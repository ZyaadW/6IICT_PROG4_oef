""" Oefening 2 (  / 4)
Bekijk kerst_oefening2.csv. Het bevat de scores die juryleden (rij 1) hebben gegeven in een wedstrijd.
Er waren in totaal 5 deelnemers die beoordeeld zijn (rij 2-6).

In de volgende stappen zal je dit bestand inlezen, verwerken en wegschrijven.
Vergeet niet bij iedere regel code commentaar te schrijven.
"""

""" STAP 1:
Lees kerst_oefening2.csv in, in een variabele van Python. 
"""
import csv #importeer csv module 

fp = open("kerstexamen_deel1/kerst_oefening2/kerst_oefening2.csv", "r") # open bestand in read modus volgens dit pad

csv_reader = csv.reader(fp, delimiter=',')  #plaats argumenten in de functie reader en zet die in de variabele



""" STAP 2:
print voor IEDERE deelnemer zijn scores af. 

VOORBEELD (jou print hoeft niet exact hetzelfde te zijn):
    Deelnemer 1 kreeg volgende scores: 9, 8, 9, 10
    ...
    Deelnemer 5 kreeg volgende scores: 7, 4, 6, 7
"""
# for rij in csv_reader:
    
#     print(rij[1])

# print(f"Deelnemer 1 kreeg volgende scores: } ")
# print(f"Deelnemer 2 kreeg volgende scores: ")
# print(f"Deelnemer 3 kreeg volgende scores: ")
# print(f"Deelnemer 4 kreeg volgende scores: ")
# print(f"Deelnemer 5 kreeg volgende scores: ")
""" STAP 3: 
Bereken voor iedere deelnemer de gemiddelde score. 
    Tip: Ieder element in een CSV-bestand is een string. Zet deze eerst om, vooraleer iets te berekenen.



Lukt dit niet?
    Je zult de gemiddelde score nodig hebben voor stap 4. 
    Bereken de gemiddelde score van iedere persoon manueel en voeg deze zelf toe aan de code (bvb. in een lijst).
    Doe je dit, dan krijg je geen punten op STAP 3.
"""


""" STAP 4:
Maak een nieuw bestand kerst_oefening2_verwerkt.csv aan. Dit bestand bevat alle kolommen van kerst_oefening2.csv.
Voeg er nog een nieuwe kolom aan toe. Deze bevat de gemiddelde score van iedere deelnemer (bepaald in STAP 3).

Een voorbeeld van het resultaat is te vinden in kerst_voorbeeld2.csv
"""
fp = open( "kerstexamen_deel1/kerst_oefening2/kerst_oefening2.csv", "w", newline="") # open nieuw bestan en stop in variabele
csv_writer = csv.writer(fp , delimiter=";") # schrijf met deze functie en stop in variabele


fp.close() # sluit csv bestand