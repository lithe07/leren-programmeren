aantal_lijsten = int(input("Voer het aantal lijstjes in: "))
lege_lijst =[]
start = 1
for lijst in range(1, aantal_lijsten + 1):
    lengte_lijst = int(input(f"Voer de lengte in voor lijst {lijst}: "))
    lijstje = list(range(start, start + lengte_lijst,1))
    start += 1
    lege_lijst.append(lijstje)
    print(f"Lijst {lijst}: {lijstje}")
print(lege_lijst)