# aantal_lijstjes = int(input("Voer het aantal lijstjes in: "))

# lijstjes = []

# for i in range(1, aantal_lijstjes + 1):
#     lengte_lijstje = int(input(f"Voer de lengte in voor lijst {i}: "))
#     lijst = []  

#     for j in range(lengte_lijstje):
#         element = j + i  
#         lijst.append(element)

#     lijstjes.append(lijst)

# for i, lijst in enumerate(lijstjes, start=1):
#     print(f"Lijst {i}: {lijst}")





# Vraag het aantal lijstjes
aantal_lijstjes = int(input("Voer het aantal lijstjes in: "))
legge_lijst

# Loop door het aantal lijstjes en vraag de lengte van elk lijstje
for i in range(1, aantal_lijstjes + 1):
    lengte_lijstje = int(input(f"Voer de lengte in voor lijst {i}: "))2

    # Genereer en toon het lijstje met de gekozen lengte en stappen
    lijstje = list(range(1, lengte_lijstje * i + 1, i))
    print(f"Lijst {i}: {lijstje}")
