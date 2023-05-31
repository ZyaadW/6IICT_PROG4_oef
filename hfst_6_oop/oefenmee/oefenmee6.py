class Hond:
        def __init__(self,naam,massa):
          self.naam = naam
          self.massa = massa     

        def blaf(self):
            print(f"{self.naam} zegt blaf")

        def weegschaal(self):
            print(f"{self.naam} weegt {self.massa}kg")

hond = Hond("Floris","8")
hond.blaf()
hond.weegschaal()

hond_2 = Hond("Fido","3")
hond_2.blaf()
hond_2.weegschaal()