import json, requests 

antwoord = requests.get("https://api.covid19api.com/world/total").text
antwoord_dict = json.loads(antwoord)
print(antwoord_dict)

fp = open("hfst_2/oefen_mee/oefen_mee15.json", "w")    
json.dump(antwoord_dict,fp)  

fp.close()