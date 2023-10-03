# voornaam = Lithe
# achternaam = Jnaid
# opdarcht = Pizza calculator

# Prijzen voor Pizza soorten.
PIZZA_PRIJZEN = {
    "groot" : 8.50,
    "medium" : 10.50,
    "klein" : 12.50
}

# Hier is de invoer van de gebruiker voor pizza soorten
aatnal_groot = int(input("Hoeveel groot pizza's wilt uw bestellen? "))
aantal_medium = int(input("Hoeveel medium pizza's wilt uw bestellen? "))
aantal_klein = int(input("Hoeveel klein pizza's wilt uw bestellen? "))

# Berekeningen van pizza prijzen 
kosten_groot = aatnal_groot * PIZZA_PRIJZEN["groot"]
kosten_medium = aantal_medium * PIZZA_PRIJZEN["medium"]
kosten_klein = aantal_klein * PIZZA_PRIJZEN["klein"]
totaal_prijs = kosten_groot + kosten_medium + kosten_klein

# dat is de bonnetje van de bestelde pizza van de gebruiker
print("===== UW Bestelling=====")
print(f"{aatnal_groot} x groot pizza's: € {kosten_groot}")
print(f"{aantal_medium} x medium pizza': € {kosten_medium}")
print(f"{aantal_klein} x klein pizza's: € {kosten_klein}")
print(f"Totaal prijs: € {totaal_prijs}")