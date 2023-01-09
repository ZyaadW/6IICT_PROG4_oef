""" Oefening 6 (  / 3)
Onderstaande code implementeert het spel woordzoeker.
Hier zal een gebruiker een willekeurig (Engels) woord proberen raden.
Maak het programma beter bestand tegen fouten door de 2 stappen te volgen.

Je moet enkel commentaar schrijven bij code die je zelf hebt geschreven.
"""

import requests

""" STAP 1:
In onderstaande functie moet de gebruiker een woord ingeven. Raise in deze functie volgende errors:
    - TypeError als het ingegeven woord karakters bevat die geen letters zijn.
                TIP: gebruik hiervoor de string methode isalpha.
    - IndexError als de LENGTE van het ingegeven woord niet gelijk is aan de moeilijkheid.
Schrijf duidelijk bij de error waarom deze geraised is.
"""
def geef_woord_in(moeilijkheid): # De waarde van moeilijkheid is een geheel getal.
    ingegeven_woord = input("Welk woord zoeken we: ") # typ een woord
    if (ingegeven_woord().isalhpa()) == True: # als het ingegeven woord in het alfabet staat
        raise TypeError("het ingegeven woord karakters bevat geen letters") #geef deze foutmelding
    if (len(ingegeven_woord)!= moeilijkheid): # als de lengte niet gelijk is aan de moeilijkheid
        raise IndexError("de lengte van het ingegeven woord is niet gelijk aan de moeilijkheid")     # geef deze foutmelding
    return ingegeven_woord # geef het woord terug





""" STAP 2: 
Vang onderstaande specifieke errors op in de instellingen (beschrijf het probleem zo duidelijk mogelijk).
Enkel als er GEEN exception optreedt, mag alle code onder START SPEL uitgevoerd worden.
    - De gebruiker geeft geen geheel getal op in moeilijkheid (ValueError).
    - Geen verbinding met de API (requests.exceptions.ConnectionError)
    - Vang alle andere mogelijke problemen op met een algemene exception.
"""

# INSTELLINGEN
try: # probeer dit

    moeilijkheid = int(input("Hoeveel letters in te zoeken woord: "))
    url = f"https://random-word-api.herokuapp.com/word?length={moeilijkheid}"
    te_zoeken_woord =  requests.get(url).text[2:-2]
    print(f"ENKEL voor ontwikkelaars. Het te_zoeken_woord is {te_zoeken_woord}\n")
except ValueError: # behalve bij deze foutmelding 
    print("geen geheel getal gekozen")  # print dit
except requests.exceptions.ConnectionError: # behalve bij deze foutmelding   
    print("geen verbinding met de API") # print dit bij de foutmelding
except Exception: # behlave bij bij algemene fouten
    print(" er is een onbkende fout opgetreden") # print dit
# EINDE INSTELLINGEN
else: # anders
    print("er zijn geen fouten opgepoord") # print dit
# START SPEL
for ronde in range(moeilijkheid):
    print(f"RONDE {ronde+1}/{moeilijkheid}")

    ingegeven_woord = geef_woord_in(moeilijkheid)


    # VERGELIJKEN WOORDEN
    for index, letter in enumerate(ingegeven_woord):
        if letter == te_zoeken_woord[index]:
            print(f"{letter} staat op de juiste positie.")
        elif letter in te_zoeken_woord:
            print(f"{letter} komt voor in woord, maar staat op verkeerde positie.")
        else:
            print(f"{letter} zit niet in woord.")
    if te_zoeken_woord == ingegeven_woord:
        print(f"Je hebt het woord '{te_zoeken_woord}' geraden!")
        break
    # EINDE VERGELIJKEN WOORDEN




    print("------------------")
else:
    print(f"Je hebt het woord niet gevonden. Het woord was '{te_zoeken_woord}'.")
