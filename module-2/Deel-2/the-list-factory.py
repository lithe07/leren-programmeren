aantal_lijstjes = int(input("Voer het aantal lijstjes in: "))

lijstjes = []

for i in range(1, aantal_lijstjes + 1):
    lengte_lijstje = int(input(f"Voer de lengte in voor lijst {i}: "))
    lijst = []  

    for j in range(lengte_lijstje):
        element = j + i  
        lijst.append(element)

    lijstjes.append(lijst)

for i, lijst in enumerate(lijstjes, start=1):
    print(f"Lijst {i}: {lijst}")
