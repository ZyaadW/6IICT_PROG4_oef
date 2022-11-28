fruit_lijst = ["Appel", "Banaan", "Kers"]

try:
    getal = input( "Geef een getal: " )
    if "." in getal:
        getal = float( getal )
    else:
        getal = int( getal )
    print( fruit_lijst[getal] )
except ZeroDivisionError:
    print("Het getal 0 kan niet worde opegegeven") 
except ValueError:
    print("De ingegeven waarde is geen getal")
except IndexError:
    print("de index ligt buiten de lijst")    
except:
    print( "Er ging iets fout" )  

print("Programma klaar")  
