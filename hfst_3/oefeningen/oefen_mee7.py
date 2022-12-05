""" Niveau 1 """
num_lijst = [ 100, 101, 0, "103", 104 ]
try:
    index = int( input( "Geef een index: " ) )
except TypeError:
    print("ingegeven waarde is geen geheel getal")
except IndexError:
    print("index ligt buiten bereik")
except ValueError:
    print("De ingegeven waarde is geen getal")
else:
    try:
        # """ Niveau 2 (haal uit commentaar) """
        print( f"100 / {num_lijst[index]} = {100/num_lijst[index]}" ) 
    except TypeError:
        print("ingegeven waarde is geen geheel getal")
    except IndexError:
        print("index ligt buiten bereik")
    except ValueError:
        print("De ingegeven waarde is geen getal") 
    except ZeroDivisionError:
        print("Het getal 0 kan niet worden opgegeven")
# """ Niveau 3 (haal uit commentaar) """
finally:
    print( "Het programma is beëndigd")