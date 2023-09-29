totaal_croissantjes= 17
totaal_stokbroden= 2


PRIJS_VAN_CROISSANTJE = 0.39
PRIJS_VAN_STOKBRODEN = 2.78


aantal_kortingsbonnen = 3 
KORTINGSBONNEN = 0.50

uitkomst_croissantjes = totaal_croissantjes * PRIJS_VAN_CROISSANTJE
uitkomst_stokbroden = totaal_stokbroden * PRIJS_VAN_STOKBRODEN
uitkomst_kortingsbon = aantal_kortingsbonnen * KORTINGSBONNEN


totaal = (uitkomst_croissantjes + uitkomst_stokbroden) - uitkomst_kortingsbon
print(f"De feestlunch kost je bij de bakker {totaal.__round__(1)} euro voor de {totaal_croissantjes} croissantjes en de {totaal_stokbroden} stokbroden als de {aantal_kortingsbonnen} kortingsbonnen nog geldig zijn!  ")



