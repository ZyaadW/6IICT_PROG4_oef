class Bankrekening: # class wordt aangemaakt
        bank = "KBC"

        def __init__(self,eigenaar,geld,leeftijd):
              self.eigenaar = eigenaar
              self.geld = geld
              self.leeftijd = leeftijd

        def storten(self, bedrag, reden):
            print(f"{bedrag+self.geld} euro afgehaald. Reden: {reden} ")

        def afhalen(self,bedrag, bericht,leeftijd):
          if leeftijd >= 16:
            print(f"{self.geld-bedrag} euro afgehaald. Reden: {bericht}")  
          else:
              print("Eigenaar is te jong om geld af te halen")  

        def overzichtelijk(self,eigenaar,bank):
            print(f"{eigenaar} heeft {self.geld} staan bij {bank}.") # functies worden aangemaakt

storting = Bankrekening(1000,"De storting is gelukt!")
afhaling = Bankrekening(500, "De afhaling was succesvol!",18)
overzicht = Bankrekening("Piet") 

storting.storten(storting) # functies worden gebruikt
afhaling.afhalen(afhaling)
overzicht.overzichtelijk(overzicht)
            