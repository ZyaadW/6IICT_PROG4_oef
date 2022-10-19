import json

fp = open("hfst_2/oefen_mee/oefen_mee9.json", "r")
quiz = json.load(fp)
fp.close()

print(quiz)

for key,onderwerp in quiz["quiz"].items():
    for key2, vraag in onderwerp.items():
        print(vraag["vraag"])
        print(vraag["opties"])
        
        keuze = input("Kies een antwoord: ")
        if keuze == vraag["antwoord"]:
            print("Het antwoord is correct!")
        else: 
            print("Het antwoord is niet correct.")   