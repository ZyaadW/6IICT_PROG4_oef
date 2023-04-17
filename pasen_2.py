""" Oefening 2: verbeter onderstaande sentimentanalyse.

Onderstaande code implementeert een sentimentanalyse. Er staan echter 2 fouten in de code. 
In deze oefening moet je volgende zaken doen:
    - Leg bij iedere fout uit wat het probleem is.
    - Los het probleem op.
    - Bepaal de sentimentscore (en vul in onderstaand teksveld aan).

DE SENTIMENTSCORE IS: 3,2
"""

""" De modules inladen is GEEN onderdeel van de fouten. 
    Indien nodig kan je onderstaande commando's gebruiken om deze in te laden:
    - pip install spacy 
    - python -m spacy download nl_core_news_sm
"""
import json, spacy
nlp = spacy.load("nl_core_news_sm")

# Open de lexicon.
with open("pasen_2_lexicon.json", "r") as file: # je probeerde iets toe te voegen in plaats van te lezen
    lexicon = json.load(file)

# Tekst waarop sentimentanalyse wordt toegepast.
tekst = "Eieren zoeken in alle hoeken, een tafel vol heerlijkheid. Zo moet Pasen zijn, een gezellig familie festijn."

# Verwerk de tekst met behulp van spacy.
tekst_verwerkt = nlp(tekst.lower())

# Plaats de woordsoorten en lemmas in aparte lijsten.
woordsoorten, lemmas  = [], []
for index, token in enumerate(tekst_verwerkt):
    woordsoorten.append(token.pos_)
    lemmas.append(token.lemma_)
    
# Bepaal (en print) de sentimentscore.
for index, lemma in enumerate(lemmas):
    sentiment_score = 0
    if lemma not in lexicon:
        continue
    sentiment_score += lexicon[lemma].get(woordsoorten[index], 0)
print(f"De sentimentscore van de review is: {sentiment_score}")