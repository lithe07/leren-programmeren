def naam_en_leeftijd():
    naam = input("Wat is je naam? ")
    leeftijd = int(input("Wat is je leeftijd? "))
    gegevens = {
        'naam': naam,
        'leeftijd' : leeftijd
    } 
    return gegevens

def gegevens_verzamelen():
    verzamel = []
    while True:
        stop_of_door = input("Wil je stoppen (j/n)? ")
        if stop_of_door == "j":
            break
        verzamel.append(naam_en_leeftijd())
    return  verzamel

data = gegevens_verzamelen()
for i in range(len(data)):
    print(f"{data[i]['naam']} is {data[i]['leeftijd']} jaar")