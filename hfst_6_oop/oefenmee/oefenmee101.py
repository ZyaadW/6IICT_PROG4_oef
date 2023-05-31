import random
locaties = ["living", "tuin", "buren", "keuken"]
class Hond:
    
   

    def __init__(self,naam,locatie):
       self.naam = naam
       self.locatie = locatie
      
    def ziet_hond(self, andere_hond):
      if self.locatie == andere_hond.locatie:
         keuze = random.choice([self,andere_hond])
         keuze.locatie = random.choice(locaties)
         
         print(f"{keuze.naam} is bang en rent naar {keuze.locatie} ")
         print(f"{self.naam} ziet {andere_hond.naam}")
      else:
         print(f"{self.naam} ziet {andere_hond.naam} niet de {self.locatie}")


hond_1 = Hond("Lulu", "keuken")
hond_2 = Hond("Floris", "keuken")
hond_3 = Hond("Ranger", "tuin")

hond_1.ziet_hond(hond_2)
hond_1.ziet_hond(hond_3)
