def vraag_aantal(pizza_soort):
    while True:
        try:
            aantal = float(input(f"Hoeveel {pizza_soort} pizza's wilt u bestellen? "))
            if aantal < 0:
                print("Aantal pizza's kan niet negatief zijn. Probeer opnieuw.")
            else:
                return aantal
        except ValueError:
            print("Ongeldige invoer. Voer een geldig getal in.")
 
def bereken_kosten(aantal, prijs):
    return aantal * prijs
 
 
PIZZA_PRIJZEN = {
    "groot": 8.50,
    "medium": 10.50,
    "klein": 12.50
}
 
aantal_per_soort = {}
for pizza_soort in PIZZA_PRIJZEN:
    aantal_per_soort[pizza_soort] = vraag_aantal(pizza_soort)
 
totaal_prijs = sum(bereken_kosten(aantal_per_soort[soort], PIZZA_PRIJZEN[soort]) for soort in PIZZA_PRIJZEN)
 
print("======= UW Bestelling=======")
for pizza_soort, aantal in aantal_per_soort.items():
    kosten = bereken_kosten(aantal, PIZZA_PRIJZEN[pizza_soort])
    print(f"{aantal} x {pizza_soort} pizza's: € {kosten}")
print("============================")
print(f"Totaal prijs: € {totaal_prijs}")
 