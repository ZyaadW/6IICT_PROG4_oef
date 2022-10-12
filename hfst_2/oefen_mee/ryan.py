import csv

fp = open( "hfst_2/oefen_mee/volcanic-eruptions-US.csv", "r" )
csv_reader = csv.reader( fp , delimiter=";") # 

for rij in csv_reader: #alle rijen van het doc worden overlopen
    print(rij[1], rij[4]) # hier wordt alles uitgeprint

fp.close() # Na sluiten is CSV niet meer bruikbaar