import json

fp = open("hfst_2/oefen_mee/oefen_mee12.json", "r")
agenda = json.load(fp)
fp.close()

keuze_dag = input("kies een dag: ")
vraag = input("Wilt u de activiteit v/d dag overschrijven j/n? ")
if vraag == "j":
    activiteit = input(f"Kies een andere activiteit voor {keuze_dag}: ")
    agenda[keuze_dag] = activiteit
    fp = open("hfst_2/oefen_mee/oefen_mee12.json", "w")
    json.dump(agenda,fp)
    fp.close()
    print(agenda)
else:
    print(agenda)    
    