import csv
#Deel 1: lees bestand in Python
fp = open("hfst_2/oefen_mee/volcanic-eruptions-EU.csv", "r")

csv_reader = csv.reader( fp , delimiter=";")

eruptions_ll = []
for rij in csv_reader:
    eruptions_ll.append(rij)

fp.close()

print("")

#Deel 2 : verwerk lijst van lijsten
print(eruptions_ll)

eruptions_ll_verwerkt = []

for index, rij in enumerate(eruptions_ll):
    if index == 0:
        eruptions_ll_verwerkt.append([rij[1], rij[4]])
    else:
        eruptions_ll_verwerkt.append([abs(int(rij[1])),rij[4].lower()])

print(eruptions_ll_verwerkt)

#Deel 3: Schrijf verwerkte lijst van lijsten weg

fp = open( "hfst_2/oefen_mee/kritieken_to_csv.csv", "w", newline="")
csv_writer = csv.writer(fp , delimiter=";")


for rij in eruptions_ll_verwerkt:
    csv_writer.writerow(rij)

fp.close()