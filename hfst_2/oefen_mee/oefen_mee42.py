import csv

fp = open("hfst_2/oefen_mee/volcanic-eruptions-EU.csv", "r")

csv_reader = csv.DictReader( fp , delimiter=";")

eruptions_ld = []
for rij in csv_reader:
    eruptions_ld.append(rij)

fp.close()

print("")
print(eruptions_ld)

eruptions_ld_verwerkt = []

for index, rij in enumerate(eruptions_ld):
    dictionary = {}
    dictionary ["Year"] = abs(int(rij["Year"]))
    dictionary["Name"] = rij["Name"].lower()
    eruptions_ld_verwerkt.append(dictionary)

print(eruptions_ld_verwerkt)    




