""" Opdracht 3: (  /3)
1) Vorm ranglijst_eten om naar een dictionary (zie voorbeeld). (  /2)

2) Dezelfde code moet ook werken voor andere ranglijsten, (  /1)
   zowel wanneer deze meer als minder rangen nodig hebben.
   Het maximum aantal rangen die een lijst kan hebben is 7.
   De rangen zijn A, B, C, D, E, F, G.

De totaalscore van deze toets is 10. Alle opdrachten zijn samen 9 punten waard.
Het laatste punt staat op het schrijven van code zonder foutmeldingen.
"""

ranglijst_eten = [
    ["water"],                                  # A
    ["groenten", "fruit", "soja", "granen"],    # B
    ["vis", "gevolgte", "kaas", "zuivel"],      # C
    ["rood vlees", "boter"],                    # D
    ["snoep", "zout", "alcohol", "fast food"]   # E
]
rangen = ["A","B","C","D","E","F","G"]
d = dict(zip(rangen, ranglijst_eten))
print(d)
 

# oplossing die net een beetje fout is 
# dict = {}
# for fruits, index in enumerate(ranglijst_eten):
#     for fruit in fruits:
#         value = index+1
#         if value == 1:
#             value = "A"
#         if value == 2: 
#             value = "B"
#         if value == 3:
#             value = "C"
#         if value == 4:
#             value = "D"
#         if value == 5:
#             value = "E"
#         if value == 6:
#             value = "F"
#         if value == 7:
#             value = "G"                        
#         dict[fruit] = value
# print(dict)


""" Te bekomen dictionary voor ranglijst_eten: 
{
    "A": ["water"],
    "B": ["groenten", "fruit", "soja", "granen"],
    "C": ["vis", "gevolgte", "kaas", "zuivel"],
    "D": ["rood vlees", "boter"], 
    "E": ["snoep", "zout", "alcohol", "fast food"]
}
"""

ranglijst_eten_2 = [
    ["water"],                                  # A
    ["groenten", "fruit", "soja", "granen"],    # B
    ["vis", "gevolgte", "kaas", "zuivel"],      # C
    ["rood vlees", "boter"],                    # D
    ["zout", "alcohol"],                        # E
    ["snoep", "fast food"],                     # F
    ["potgrond", "houtschors", "mos"],          # G
]

""" Te bekomen dictionary voor ranglijst_eten_2: 
{
    "A": ["water"],
    "B": ["groenten", "fruit", "soja", "granen"],
    "C": ["vis", "gevolgte", "kaas", "zuivel"],
    "D": ["rood vlees", "boter"], 
    "E": ["zout", "alcohol"],
    "F": ["snoep", "fast food"],
    "G": ["potgrond", "houtschors", "mos"],
}
"""

