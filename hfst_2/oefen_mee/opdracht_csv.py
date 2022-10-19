""" Opdracht:
Bekijk machten.csv. In dit bestand zijn drie kolommen gegeven:
    - basis: Getallen van 1 tot en met 10.
    - kwadraat: Het kwadraat van de linksgelegen basisgetallen.
    - derdemacht: De derdemacht van de linksgelegen basisgetallen.
    OPGELET: dit bestand gebruikt komma als scheidingsteken, geen punt-komma.

Momenteel zijn enkel de kolommen basis en kwadraat ingevuld.
De opdracht is als volgt:
    1) Open machten.csv in Python. Print iedere rij van de bekomen tabel. 
    2) Vul de kolom derdemacht aan in deze tabel. 
    3) Schrijf de verwerkte tabel weg naar een nieuw bestand. BVB. machten_verwerkt.csv.
OPGELET: Het verwerkte CSV-bestand moet komma's gebruiken als scheidingsteken. 

Puntenverdeling: (  / 5)
    1) Open en print machten.csv in Python (  / 1).
    2) Vul de kolom derdemacht aan in Python (  / 1).
    3) Schrijf de verwerkte tabel weg naar een nieuw bestand (  / 1).
    4) Schrijf bij iedere regel code commentaar die uitlegt wat je doet ( / 1).
    5) De ingeleverde code bevat geen foutmeldingen (  / 1).
      OPGELET: Voor onderdelen 1, 2 en 3 kijk ik enkel naar code die NIET in commentaar staat.
"""

import csv #importeer csv module

fp = open("hfst_2/oefen_mee/machten.csv", "r") # open bestand in read modus volgens dit pad

csv_reader = csv.reader(fp, delimiter=',')  #plaats argumenten in de functie reader en zet die in de variabele
lijst = []

for rij in csv_reader: # voor rij in csv_reader
    rij[2] = rij[0]**3 # formule voor rijen
    print(rij[2]) #print rij
fp.close() #sluit bestand








fp = open("toets", "w", newline="" ) #open bestand in write formaat
csv_writer = csv.writer( fp , delimiter=",") #plaats argumenten in de functie writer en zet die in de variabele

for index, rij in enumerate(lijst): #voor rij in csv_writer
    if index != 0:
        rij_verwerkt = [rij[0], rij[1], int(rij[0])**3]
    csv_writer.writerow(rij) #schrijf rij in bestand

fp.close()    #sluit bestand