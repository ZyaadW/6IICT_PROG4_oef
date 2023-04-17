""" Voorbeeldoefening: maak de gegeven GUI na (zie pasen_voorbeeld.exe).

De GUI is een "Letter-zoeker". Door op de knop te klikken zoekt het programma hoevaak
een letter voorkomt in een zin. Het verhoogt dan een teller met dit aantal.

Let zeker op volgende zaken:
    - De titel van de app is "Letter-zoeker".
    - De entry onderaan begint met een waarde gelijk aan 0.
    - De gebruikte FONT voor alle elementen is "Comic Sans MS" met een grootte van 12.
    - Als de te zoeken letter wijzigt, moet de teller terug van 0 beginnen.

Breng commentaar aan bij de code. Dit moet het doel/werking ervan uitleggen.
Je mag verschillende regels code samen uitleggen.
"""

import tkinter as tk

class LetterCounterGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Letter Counter")

        # Maak het invoervak voor tekst
        self.textbox = tk.Entry(self.window)
        self.textbox.pack()

        # Maak de knop voor tellen
        self.count_button = tk.Button(self.window, text="Tellen", command=self.count_letters)
        self.count_button.pack()

        # Maak het uitvoervak voor resultaten
        self.result_label = tk.Label(self.window)
        self.result_label.pack()

        self.window.mainloop()

    def count_letters(self):
        # Haal de tekst op uit het invoervak
        text = self.textbox.get()

        # Initialiseer de teller
        counts = {}

        # Loop door elk karakter in de tekst en tel het aantal keer dat het voorkomt
        for char in text:
            if char in counts:
                counts[char] += 1
            else:
                counts[char] = 1

        # Zet de resultaten om in een string en toon deze in het uitvoervak
        result_str = "\n".join([f"{char}: {count}" for char, count in counts.items()])
        self.result_label.config(text=result_str)

if __name__ == "__main__":
    app = LetterCounterGUI()
