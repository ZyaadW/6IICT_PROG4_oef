import csv

"""Deel 1: inlezen"""
fp = open("hfst_2/oefen_mee/volcanic-eruptions-EU.csv", "r")

csv_reader = csv.DictReader( fp , delimiter=";")

eruptions_ld = []
for rij in csv_reader:
    eruptions_ld.append(rij)

fp.close()

"""Deel 2: verwerken"""

print("")
print(eruptions_ld)

eruptions_ld_verwerkt = []

for index, rij in enumerate(eruptions_ld):
    dictionary = {}
    dictionary ["Year"] = abs(int(rij["Year"]))
    dictionary["Name"] = rij["Name"].lower()
    eruptions_ld_verwerkt.append(dictionary)

print(eruptions_ld_verwerkt)    


"""Deel 3: inlezen"""
fp = open("eruptions_ld_verwerkt.csv", "w", newline="")

csv_writer = csv.DictWriter(fp, delimiter=";", fieldnames=["Year", "Name"])

csv_writer.writeheader()
for rij in eruptions_ld_verwerkt:
    csv_writer.writerow(rij)

fp.close()