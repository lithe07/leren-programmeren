
TOTAAL_CROISSANTJES= 17
TOTAAL_STOKBRODEN = 2


PRIJS_VAN_CROISSANTJE = 0.39
prijs_van_stokbrood = 2.78


AANTAL_KORTINGSBONNEN = 3 
KORTINGSBONNEN = 0.50


uitkomst_croissantjes = (TOTAAL_CROISSANTJES * PRIJS_VAN_CROISSANTJE)
uitkomst_stokbroden = (TOTAAL_STOKBRODEN * prijs_van_stokbrood)
uitkomst_kortingsbon = (AANTAL_KORTINGSBONNEN * KORTINGSBONNEN)


totaal = (uitkomst_croissantjes + uitkomst_stokbroden) - uitkomst_kortingsbon
print(f"De feestlunch kost je bij de bakker {totaal.__round__(1)} euro voor de {TOTAAL_CROISSANTJES} croissantjes en de {TOTAAL_STOKBRODEN} stokbroden als de {AANTAL_KORTINGSBONNEN} kortingsbonnen nog geldig zijn!  ")



