class Hond:
        def benoem(self,naam):
            self.naam = naam

        def blaf(self):
            print(f"{self.naam} zegt blaf")

        def wegen(self,massa):
            self.massa = massa 
        def weegschaal(self):
            print(f"{self.naam} weegt {self.massa}kg")

huisdier = Hond()
huisdier.benoem("Bert")
huisdier.blaf()

hond = Hond()
hond.benoem("Fleur")
hond.blaf()

dier = Hond()
dier.benoem("Fifi")
dier.wegen(3)
dier.weegschaal()
