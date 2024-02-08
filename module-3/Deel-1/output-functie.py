from functie_nlw import naam_en_leeftijd, gegevens_verzamelen


data = gegevens_verzamelen()

for i in range(len(data)):
    print(f"{data[i]['naam']}, die in {data[i]['woonplaats']} woont, is {data[i]['leeftijd']} jaar oud")
