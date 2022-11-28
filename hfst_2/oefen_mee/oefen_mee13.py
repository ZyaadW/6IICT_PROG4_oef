import json

fp = open("hfst_2/oefen_mee/oefen_mee13.json", "r")
data = json.load(fp)


for index,cases in enumerate(data):
    if index == 0:
        print(f"{cases['Date']} zijn er 0 nieuwe cases.")
        aantal_vorige_dag = cases["Cases"]
    else:
        verschil = cases["Cases"] - aantal_vorige_dag
        print(f"op {cases['Date']} zijn er {verschil} nieuwe cases")
        aantal_vorige_dag = cases["Cases"]
        cases["nieuwe_cases"] = verschil     
fp = open("hfst_2/oefen_mee/oefen_mee13.json", "w")    
json.dump(data,fp)  

fp.close()