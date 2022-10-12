import csv # importeer csv module

fp = open( "volcanic-eruptions-EU.csv", "r" ) # open bestand in read modus
# var csv_reader kan je niet rechtstreeks wijzigen of oproepen.
csv_reader = csv.reader( fp , delimiter=";")  # lees de bestand en deel de zinnen op na elke punt komma
# print(csv_reader[3]) # Voorbeeld

# Aanmaken ECHTE lijst van lijsten (ll) en hierin gegevens stoppen
eruptions_ll = [] # lege lijst aanmaken
for rij in csv_reader: # doorloop alle rijen in csv reader
    eruptions_ll.append(rij) # voeg rijen toe aan lijst

fp.close() # Na sluiten is CSV niet meer bruikbaar

for eruption in eruptions_ll: 
    print(eruption) # print de lijsten

import csv

fp = open( "volcanic-eruptions-EU.csv", "r" )
csv_reader = csv.DictReader( fp , delimiter=";")

eruptions_ld = [] # ld = lijst van dictionaries
for rij in csv_reader:
    print(rij)
    eruptions_ld.append(rij)

fp.close() # Na sluiten is CSV niet meer bruikbaar

print("")
print(eruptions_ld)
