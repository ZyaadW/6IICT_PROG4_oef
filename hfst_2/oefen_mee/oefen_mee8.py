import json

fp = open("hfst_2/oefen_mee/oefen_mee8.json", "r")
appel = json.load(fp)
fp.close()

keuze_dag = input("kies een dag: ")
print(appel[keuze_dag])