def maak_persoonsinformatie_dict(naam, leeftijd, massa, lengte, oogkleur):
    """Geef een dictionary terug met alle gegevens die als parameters aan
    de functie meegegeven werden.
    
    >>> maak_persoonsinformatie_dict("Jan", 32, 79, 167, "blauw")
    {'naam': 'Jan', 'leeftijd': 32, 'massa': 79, 'lengte': 167, 'oogkleur': 'blauw'}
    """
    persoon_info = {"naam": naam, "leeftijd": leeftijd, "massa": massa, "lengte": lengte, "oogkleur": oogkleur}
    
    return(persoon_info)

print(maak_persoonsinformatie_dict("Jan", 32, 79, 167, "blauw"))
