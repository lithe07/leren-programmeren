def vraag_naam_leeftijd():
    naam = input("Wat is je naam? ")
    leeftijd = int(input("Wat is je leeftijd? "))
    gegevens = {
        'naam': naam,
        'leeftijd' : leeftijd
    } 
    return gegevens

resultaat = vraag_naam_leeftijd()
print(f"{resultaat['naam']} is {resultaat['leeftijd']} jaar")