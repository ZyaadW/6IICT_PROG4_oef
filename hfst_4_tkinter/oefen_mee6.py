import tkinter as tk

venster = tk.Tk()

# Functie maakt een label aan wanneer opgeroepen.
def knop_klik():
    knop = tk.Button(master=venster, text="Goed gedaan!", command=knop_klik)
    knop.pack()

# Knop aanmaken.
    # master: geef aan tot welke GUI de knop behoort.
    # text: boodschap van de knop.
    # command: aan welke functie is de knop gelinkt.
knop = tk.Button(master=venster, text="Klik op mij!", command=knop_klik)

knop.pack()

venster.mainloop()
