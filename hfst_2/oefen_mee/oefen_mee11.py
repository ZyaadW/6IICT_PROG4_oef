import json

person_dict = {
    "naam": "Gert",
    "talen": ["Nl", "En"],
    "getrouwd": True,
    "leeftijd": 33}

# Maakt nieuw persoon.json aan in pad
fp = open("hfst_2/oefen_mee/oefen_mee11.json", "w")
json.dump(person_dict, fp)
fp.close() # Na sluiten is JSON niet meer bruikbaar