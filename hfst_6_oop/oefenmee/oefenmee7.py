class Hond:
        def __init__(self,naam,massa):
          self.naam = naam
          self.massa = massa     
        def wijzig_naam(self,nieuwe_naam):
             print(f"{self.naam} heet nu {nieuwe_naam}")
             self.naam = nieuwe_naam
             
        def blaf(self):
            print(f"{self.naam} zegt blaf")

        def eten(self,nieuw_gewicht):
            self.massa = self.massa + nieuw_gewicht
            print(f"{self.naam} weegt {self.massa}kg")

hond = Hond("Lucky",5)
hond.eten(2)
hond.wijzig_naam("Jarne peeters")
hond.eten(2)

huisdier= Hond("Adam",69)
huisdier.wijzig_naam("Figlio")
huisdier.eten(2)