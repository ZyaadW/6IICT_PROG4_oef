" Goed gedaan. Kijk STAP 3 van oefening 1 na. Ik heb hier een aantal voorbeeldoplossingen gegeven." 

""" Algemeen (gaat over oefening 1 en 2): ( 2 / 2)
Schrijf bij iedere regel code commentaar ( 1 / 1)
Zorg dat de code geen geeft foutmeldingen ( 1 / 1)
    Opgelet! Code in commentaar wordt niet bekeken.
"""
import json, random # importeer het json-module en random-module
""" OEFENING 1: ( 3 / 5)
oefening1.json bevat info over Warren Buffett.
Dit is een zeer bekende investeerder.
"""
fp = open("oefening1.json", "r") # de variabele "fp" gelijk aan het openen van het json bestand in de read-modus
info = json.load(fp) #zet de variabele "info" gelijk aan dat het bestand ingeladen wordt als json

fp.close() # # Na sluiten is JSON niet meer bruikbaar
""" STAP 1: ( 1 / 1)
laad oefening1.json in Python. Zet deze dictionary in een variabele.
Gebruik voor beide delen de JSON-module van Python.

Lukt dit niet? Dan mag je de dictionary rechtstreeks in de variabele plakken.
               Je krijgt dan wel geen punten voor dit onderdeel.
"""
" De haken () rond info zijn niet nodig. "
a = (info["voornaam"]) # haal de value van "voornaam" uit de dict 
b = (info["geboortedatum"]) # haal de value van "geboortedatum" uit de dict 
c = (info["bedrijf"]) # haal de value van "bedrijf" uit de dict 
" Leuke oplossing! "
d = (info["hobbys"][random.randint(0,3)]) # haal de value van "hobbys" uit de dict EN kies 1 van de 4 elementen met de random-module

print(f"{a} is geboren op {b}. Hij is de eigenaar van {c}. Hiernaast speelt hij ook {d}.") # print met een f-string alle variabelen uit
""" STAP 2: ( 1 / 1)
print volgende zaken van Warren Buffett in een grote f-string:
    - voornaam
    - geboortedatum
    - bedrijf
    - 1 hobby (bvb. deze op index 3)

Je moet deze info uit de dictionary halen (dus niet manueel invullen).

De print kan er als volgt uit zien:
Warren is geboren op 03-08-1930. Hij is de eigenaar van Berkshire Hathaway. Hiernaast speelt hij ook ukelele.
"""


""" STAP 3: ( 0 / 2)
Gebruik code om het minimale en maximale vermogen in de laatste 5 jaar (2017-2021) te bepalen.
Ook als de cijfers van het vermogen zouden wijzigen, moet de code blijven werken.
    Tip: je kan de functies min() en max() toepassen op lijsten. Dit geeft de kleinste/grootste waarde terug.

Lukt dit niet? Dan mag je het minimale en maximale vermogen zelf bepalen.
               Je krijgt dan wel slechts een deel van de punten voor dit onderdeel

Voeg dit minimale en maximale vermogen toe als value aan de hoofddictionary. 
Gebruik hiervoor de keys verm_min en verm_max.
"""
# info["vermogen_in_miljard"]["2017"] =  
" Spijtig dat dit niet gelukt is. Ik geef je hier twee mogelijke oplossingen mee. "

""" OPLOSSING 1:
vermogen = info["vermogen_in_miljard"] # Haal de subdict "vermogen_in_miljard" uit de dict info. Zet deze subdict in de variabele vermogen.
minimaal, maximaal = min(vermogen.values()), max(vermogen.values()) # Bereken de min/max WAARDE van de vermogens.
info["min_verm"] = minimaal # Voeg minimale waarde toe aan dict info.
info["max_verm"] = maximaal # Voeg maximale waarde toe aan dict info.

"""

""" OPLOSSING 2:
lijst = [] # Maak een lege lijst aan.
for key, value in variabele["vermogen_in_miljard"].items():  # Overloop alle items in de subdict "vermogen_in_miljard"
    lijst.append(value) # Voeg de waarde toe aan de lijst.
info["min_verm"] = min(lijst) # Voeg minimale waarde toe aan dict info.
info["max_verm"] = max(lijst) # Voeg maximale waarde toe aan dict info.

"""

""" STAP 4: ( 1 / 1)
Schrijf de gewijzigde dictionary weg naar een NIEUW JSON-bestand.
Bijvoorbeeld oefening1_resultaat.json .
"""
fp1 = open("oefening1_resultaat.json", "w") # stel de variabele "fp1" gelijk aan een nieuw write-bestand

json.dump(info, fp1) # dump de aangepaste dict naar het nieuwe bestand

fp.close() # Na sluiten is JSON niet meer bruikbaar
