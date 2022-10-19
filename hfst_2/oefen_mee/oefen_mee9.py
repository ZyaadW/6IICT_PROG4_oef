import json

fp = open("hfst_2/oefen_mee/oefen_mee8.json", "r")
quiz = json.load(fp)
fp.close()

print(quiz)