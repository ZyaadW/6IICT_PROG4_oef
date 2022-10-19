import time #importeer tijd
import board #importeer bord
import adafruit_dht #importeer dht11
import math #importeer module math
somTemp= 0 #de optelling van alle temperaturen
somVocht = 0 #de optelling van alle vochten
temp_K = 0 # het aantal keren dat de temperaturen voorkomen
vocht_K = 0 # het aantal keren dat de vochten voorkomen
dhtDevice = adafruit_dht.DHT11(board.D12) # dit is de pin waar we de waardes van de dht verkrijgen en wordt geplaatst in de variabele
fp = open("DHT11_waardes", "w") #open de file DHT11_waardes als write bestand 
fp.write("|          tijd            |          vochtigheid           |           temperatuur         |        gemiddelde temp          |         gemiddelde vocht|") #schrijf dit in de file op de eerste rij
fp.close() #sluit de file

while True: # als het waar is
    try:# probeer dit
        tijd = time.ctime() #de variabele is gelijk aan deze functie
        temp = dhtDevice.temperature # de temp wordt hierin gezet
        vocht = dhtDevice.humidity # de vochtigheid wordt hierin geplaatst
        somVocht = somVocht+vocht # de optelling van de vochten + de huidige vochtigheid
        somTemp = somTemp+temp # de optelling van de temperaturen + de huidige temperatuur
        vocht_K = vocht_K+1 # de keren dat de vochtigheid voorkomt
        temp_K = temp_K+1 # de keren dat de temperatuur voorkomt
        gem_temp = somTemp/temp_K # de gemiddelde temperatuur formule
        gem_vocht = somVocht/vocht_K # de gemiddelde vochtigheid formule
        fp = open("DHT11_waardes.txt", "a") #open de file DHT11_waardes als bestand
        fp.write("\n") # schrijf een witregel
        fp.writelines(f"|    {tijd}      |       {round(vocht,2)}%       {round(temp,2)}°C        {round(gem_temp,2)}°C        {round(gem_vocht,2)}%") #schrijf deze waardes keer op keer in het file
        time.sleep(5) #wacht 5s   
    except RuntimeError as error:  # als dan dat
        print(error.args[0]) #print dit in terminal 
        time.sleep(2.0) #delay
        continue # ga naar volgende
    except Exception as error: # als dan dat
        dht.exit() # sluit dht
        raise error # terug naar andere except
    time.sleep(2) # wacht 2s