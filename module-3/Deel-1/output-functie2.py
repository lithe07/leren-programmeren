from functie_nlw import naam_en_leeftijd, gegevens_verzamelen


data = gegevens_verzamelen()

for i in range(len(data)):
    print(f"In {data[i]['woonplaats']} woont de {data[i]['leeftijd']} jarige {data[i]['naam']}")
    
