def vraag_naam_leeftijd():
    naam = input("Wat is je naam? ")
    leeftijd = int(input("Wat is je leeftijd? "))
    woonplaats = input("Waar woon je? ")
    gegevens = {
        'naam': naam,
        'leeftijd' : leeftijd,
        'woonplaats': woonplaats
    } 
    return gegevens

def gegevens_verzamelen():
    verzamel = []
    while True:
        stop_of_door = input("Wil je stoppen (j/n)? ")
        if stop_of_door == "j":
            break
        verzamel.append(vraag_naam_leeftijd())
    return  verzamel

data = gegevens_verzamelen()
for i in range(len(data)):
    print(f"{data[i]['naam']}, die in {data[i]['woonplaats']} woont, is {data[i]['leeftijd']} jaar")