aantal_croissantjes= int(input("Hoeveel croissantjes wil je bestellen? ")) 
aantal_stokbroden= int(input("Hoeveel stokbroden wil je bestellen? "))


prijs_van_croissantje = float(input("Wat is de prijs van een croissantje? "))
prijs_van_stokbroden = float(input("Hoeveel is de prijs van een stokbrood? "))


aantal_kortingsbonnen = int(input("Hoeveel aantal kortingsbonnen heb je? ")) 
kortingsbonen = int(input("wat is de prijs van een kortingbon? "))



uitkomst_croissantjes = aantal_croissantjes * prijs_van_croissantje
uitkomst_stokbroden = aantal_stokbroden * prijs_van_stokbroden
uitkomst_kortingsbon = aantal_kortingsbonnen * kortingsbonen


totaal = (uitkomst_croissantjes + uitkomst_stokbroden) - uitkomst_kortingsbon 
print(f"De feestlunch kost je bij de bakker {totaal} euro voor de {aantal_croissantjes} croissantjes en de {aantal_stokbroden} stokbroden als de {aantal_kortingsbonnen} kortingsbonnen nog geldig zijn!  ")
