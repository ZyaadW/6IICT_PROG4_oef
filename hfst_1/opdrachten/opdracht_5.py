poll_talen = ["Lucas", "Maud", "Jan", "Dillan", 
              "Piet", "Joris"]

favorite_languages = {    
    "Jan": "python",    
    "Piet": "c",    
    "Joris": "ruby"}

for namen in poll_talen:
    if namen in favorite_languages:
        print(f"Dankuwel voor uw deelname {namen}")
    else:
        print(f"Neem deel aan de poll {namen}")
        a = input("Geef iets in")
        if a !=  '':
            print(a) 
            favorite_languages[namen] = a 
    
print(favorite_languages)                    