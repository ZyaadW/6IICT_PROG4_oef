# Importeer tkinter module. Geef naam tk.
import tkinter as tk

# Vraag om de lievelingskleur van de gebruiker (rood, groen of blauw)
kleur = input("Wat is je favoriete kleur? ")

# Maak een lege GUI aan.
venster = tk.Tk()
vertaling= {
    "groen":"green",
    "blauw":"blue",
    "rood":"red"
}

# TODO: vertaal input van gebruiker naar het Engels

# TODO: maak functie aan die het label in de ingegeven kleur laat zien.
def knop_klik():
    knop = tk.Label(master=venster, text= f"{kleur} is mijn favoriete kleur", foreground= vertaling[kleur])
    knop.pack()

knop = tk.Button(master=venster, text="Klik op mij!", command=knop_klik )
knop.pack()

# Maak de GUI zichtbaar op de computer.
venster.mainloop()