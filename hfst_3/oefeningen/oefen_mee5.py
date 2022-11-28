""" Niveau 1 & 2
Wat gaat hier mis?
"""
fruit_lijst = ["Appel", "Banaan", "Meloen", "Mango", "Druif"]
try:
    getal = int( input("Hoeveel fruit uit de lijst wil je printen: ") )

 
    for i in range(getal):
        fruit = fruit_lijst[i]
        print(fruit)
except IndexError:
    print("de index ligt buiten de lijst")
except ValueError:
    print("De ingegeven waarde is geen getal")
except ZeroDivisionError:
    print("Het getal 0 kan niet worde opegegeven")    
except: 
    print("onbekende fout is opgetreden")     

""" Niveau 3 (haal uit commentaar) """
while True:
    fruit = input("Element aan lijst toevoegen: ")
    
    if fruit == "":
        break # Loop stopt wanneer gebruiker een lege string ingeeft.
    else:
        fruit_lijst.append(fruit)

print(fruit_lijst)
