""" Opdracht 2:
Je krijgt een lijst van lijsten genaamd landen_steden.
1) Vorm deze om naar een dictionary van lijsten.
   De eerste lijst bevat alle keys. Deze moeten gekoppeld worden aan de overige lijsten.
   
   Te bekomen dictionary:
   {
    "USA":  ["Boston", "Pittsburgh", "Washington"],
    "UK":   ["London", "Edinburgh", "Belfast"],
    "Frankrijk": ["Parijs", "Lyon", "Avignon"],
    "Duitsland: ["Keulen", "Berlijn"]
   }

2) Vraag de gebruiker om een stad. 
   Gebruik de opgestelde dictionary om het land te printen waarin deze stad zich bevindt.
   >>> input: Lyon
       Frankrijk
"""
landen_steden = [
    ["USA", "UK", "Frankrijk", "Duitsland"],    # Landen
    ["Boston", "Pittsburgh", "Washington"],     # Steden USA
    ["London", "Edinburgh", "Belfast"],         # Steden UK
    ["Parijs", "Lyon", "Avignon"],              # Steden Frankrijk
    ["Keulen", "Berlijn"]                       # Steden Duitsland
]



dict_land = {} #een lege dict
for index, land in enumerate(landen_steden[0]): #de index en positie worden door deze functie uit de lijst met begin positie 1 gehaald, en vervolgends zal die in de variabele geplaatst worden 
    dict_land[land] = landen_steden[index+1] #de dict word gevuld met de landen en die zal dat aantal keren doen totdat die alles in vol heeft, telkens word er 1 opgeteld bij de index

print(dict_land) #print de dict

stad = input("Geef een stad: ") #de variabele is gelijk aan een input van de gebruiker
for land, steden in dict_land.items(): #deze functie geeft de key en value paren van de dict en stopt die in de variabelen
    if stad in steden: #als de stad (hetgene dat je wordt gevraagd) in 1 van de values zit
        print(land) #print de landen 
else: # anders
    print("Stad niet in lijst.") # print dit als het niet zo is
