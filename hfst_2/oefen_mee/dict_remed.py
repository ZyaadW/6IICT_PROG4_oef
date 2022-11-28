""" Deze opdrachten moeten je helpen met het verwerken van dictionaries.
    Print op het einde van iedere opdracht het resultaat.

    Zet opdrachten die je afhebt in commentaar. Anders zal de terminal snel onleesbaar worden.
"""

""" Opdracht 1
Maak een dictionary met als keys "voornaam", "achternaam", "leeftijd", "hobby".
De waarde van deze keys mag je zelf invullen.
"""

""" Opdracht 2
Gebruik onderstaande dictionary. Pas de waarde van de key 1 aan.
De nieuwe waarde is "M. Verstappen".

Resultaat: {1: "M. Verstappen", 2: "S. Perez", 3: "C. Leclerc", 4: "E. Ocon"}
"""
race = {1: "???", 2: "S. Perez", 3: "C. Leclerc", 4: "E. Ocon"}

""" Opdracht 3
Print alle keys van onderstaande dictionary. Gebruik een for-loop.
"""
fruitmand = {"appel":3, "banaan":5, "kers":50, "mango":0, "aardbei": 20}

""" Opdracht 4
Vraag de gebruiker om een soort fruit. Print of dit soort fruit 
in onderstaande fruitmand voorkomt.
"""
fruitmand = {"appel":3, "banaan":5, "kers":50, "mango":0, "aardbei": 20}

""" Opdracht 5
Print alle waardes (= values) van onderstaande dictionary. Gebruik een for-loop.
"""
race = {1: "M. Verstappen", 2: "S. Perez", 3: "C. Leclerc", 4: "E. Ocon"}

""" Opdracht 6
Schrijf een programma dat onderstaande 2 lijsten naar een dictionary omzet.

Resultaat: {1: "M. Verstappen", 2: "S. Perez", 3: "C. Leclerc", 4: "E. Ocon"}
"""
plaats = [1, 2, 3, 4]
persoon = ["M. Verstappen", "S. Perez", "C. Leclerc", "E. Ocon"]

""" Opdracht 7
Verwijder de key "kers" uit onderstaande dictionary. Print de nieuwe dictionary

Resultaat: {"appel":3, "banaan":5, "mango":0, "aardbei": 20}
"""
fruitmand = {"appel":3, "banaan":5, "kers":50, "mango":0, "aardbei": 20}

""" Opdracht 8
Draai de volgorde van onderstaande dictionary om.

Resultaat: {4: "E. Ocon", 3: "C. Leclerc", 2: "S. Perez", 1: "M. Verstappen"}
"""
race = {1: "M. Verstappen", 2: "S. Perez", 3: "C. Leclerc", 4: "E. Ocon"}

""" Opdracht 9
Print de som van alle waarden in onderstaande dictionary

Resultaat: 27
"""
clubs = {"standaard": 16, "Antwerp FC": 1, "Club Brugge":3, "KAA Gent":7}

""" Opdracht 10
Combineer onderstaande 2 dictionaries tot een grote dictionary. print deze.

Resultaat:  {"appel":3, "banaan":5, "kers":50, "mango":0, "aardbei": 20}
"""
fruitmand_1 = {"appel":3, "banaan":5, "kers":50} 
fruitmand_2 = {"mango":0, "aardbei": 20}

""" Opdracht 11
Vraag de gebruiker om een club. 
    Als de club voorkomt in de dictionary, verwijder deze en print de dictionary
    Anders print "Club bestaat niet".

Input: "standaard"
Resultaat: {"Antwerp FC": 1, "Club Brugge":3, "KAA Gent":7}

Input: "Chelsea"
Resultaat: "Club bestaat niet"
"""
clubs = {"standaard": 16, "Antwerp FC": 1, "Club Brugge":3, "KAA Gent":7}

""" Opdracht 12
Haal de minimum en maximum waarde uit onderstaande dictionary.
Uit de print moet het duidelijk zijn welke waarde de kleinste, en welke de grootste is.

Resultaat: kleinste is 1, grootste is 16.
"""
clubs = {"standaard": 16, "Antwerp FC": 1, "Club Brugge":3, "KAA Gent":7}

""" Opdracht 13
Zet onderstaande lijst van lijsten om naar een dictionary.
Resultaat: {1:"a", 2:"b", 3:"c", 4:"d", 5:"e"}
"""
alfabet = [ [1, "a"], [2, "b"], [3, "c"], [4, "d"], [5, "e"] ]

""" Opdracht 14
Verwijder de keys met leestekens uit onderstaande dictionary.

Resultaat: {"waar": 8, "bronsgroen": 1, "nachtegaal": 4}
"""
freq_woord = {"waar": 8, "bronsgroen": 1, "?": 2, "nachtegaal": 4, ".": 2}

""" Opdracht 15
Print de waarde bij de key "maand".
Tip: zet onderstaande dictionary op meerdere regels. Dit maakt de structuur leesbaarder

Resultaat: "Januari"
"""
personen = {"davy": {"geslacht": "man", "woonplaats": "bree", "geboorte": {"jaar": "1968", "maand": "Januari", "dag": 24}, "Hobby": "motors" } }

""" Opdracht 16 - Afsluitende opdracht
Onderstaande lijst van dictionaries toont personen die boeken hebben geleend van de bibliotheek.
Hiernaast wordt voor iedere persoon ook getoond  hoeveel boeken ze geleend hebben en hoe groot hun boete is.

Schrijf een programma waar de gebruiker een naam kan opgeven.
Ga na of de persoon nog boeken mag lenen. Dit mag niet als: 
    - De persoon reeds 10 boeken geleend heeft.
    - De boete groter is dan 5 euro.
Print "Naam mag persoon lenen" of "Naam mag persoon niet lenen". Dit afhankelijk van de situatie.

Als de gebruiker een naam opgeeft die niet bestaat in onderstaande lijst, print dan "persoon bestaat niet".
"""
bib = [ # Naam: [Aantal boeken geleend, boete (in euro)]
    {"Alex":     [3, 0] },
    {"Brigitte": [1, 6] },
    {"Chloe":    [10, 3] },
    {"Davy":     [4, 5] },
    {"Emily":    [10, 9] }
]