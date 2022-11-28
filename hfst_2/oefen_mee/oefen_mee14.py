import requests # importeer request module

antwoord = requests.get("https://api.covid19api.com/world/total").text # haal tekst van de website
print(antwoord) # print antwoord