""" Oefening 1: maak de gegeven GUI na (zie pasen_1.exe).

De GUI is een "Klikker-spel". Door op de knop te klikken, verhoogt de gebruiker een teller.
Hoeveel de teller verhoogt, hangt af van de waarde in de Entry bovenaan.

Let zeker op volgende zaken:
    - De titel van de app is "Klikker-spel".
    - Beide Entries hebben een startwaarde gelijk aan 0.
    - De gebruikte FONT voor alle elementen is "Helvetica" met een gvensterte van 14.
    - De bovenste Entry moet als waarde een getal bevatten. 
      Is dit niet zo wanneer de gebruiker klikt? Dan reset de Entry onderaan terug naar 0.

Breng commentaar aan bij de code. Dit moet het doel/werking ervan uitleggen.
Je mag verschillende regels code samen uitleggen.
"""
import tkinter as tk # importeer de nodige modules

venster = tk.Tk()


class teller: # functie (teller) voor de knop en labels, alles aanmaken
    def __init__(self, master):
        self.master = master
        master.title("Klikker-spel")

        self.startWaarde = 0

        self.label = tk.Label(master=venster, text="Verhoog waarde met:",width=33, font=("Helvetica",14),
                  border=10, borderwidth=5)
        self.label.grid(row=0, column=0, columnspan=1)

        self.label2 = tk.Label(master=venster, text="Teller:",width=33, font=("Helvetica",14),
                  border=10, borderwidth=5)
        self.label2.grid(row=3, column=0, columnspan=1)

        self.entry = tk.Entry(master=venster, width=33, font=("Helvetica",14),
                  border=10, borderwidth=5)
        self.entry.grid(row=0, column=1)

        self.label3 = tk.Label(master=venster, text="",width=33, font=("Helvetica",14),
                  border=10, borderwidth=5)
        self.label3.grid(row=3, column=1, columnspan=2)

        self.button = tk.Button(master=venster, text="Klik", command=self.add, width=55) 
        self.button.grid(row=2, column=0, columnspan=2)
  

    def add(self): # controleer of het een geldig geheel getal is met de Add-methode
        try: # probeer
            num = int(self.entry.get())
            self.startWaarde += num
            self.label2.config(text=str(f"teller: {self.startWaarde}"))
        except ValueError: # als hij geen verkeerde waarde intypt
            self.startWaarde = 0
            self.label.config(text="Verhoog waarde met 0")

gui = teller(venster) # open het venster
venster.mainloop()