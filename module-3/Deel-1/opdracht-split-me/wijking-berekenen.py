import math

def Standaardafwijking_berekenen(getallen):
    aantal = len(getallen)
    gemiddelde = sum(getallen) / aantal
    verschil_kwadraat = sum((x - gemiddelde) ** 2 for x in getallen)
    variantie = verschil_kwadraat / aantal
    standaardafwijking = math.sqrt(variantie)
    return standaardafwijking, variantie

getallenlijst = [16, 2, 5, 8, 12, 3, 9, 16, 5, 8, 64, 33]
berekening, variantie =  Standaardafwijking_berekenen(getallenlijst)
print("De standaard afwijkingen van de getallen zijn:", berekening)


# de naam van functie moet beginnen met een werkwoord en de uitkomst