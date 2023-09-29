aantal_mensen = 4

TOEGANGTICKET_PER_PERSOON = 7.45
GAMESEAT_PER_5_MINUUT = 0.37
TIJD_GAMESEAT_MINUTEN = 45
PERIODE = 5

totaal_kosten_gameseat = ((TIJD_GAMESEAT_MINUTEN / PERIODE) * GAMESEAT_PER_5_MINUUT) * aantal_mensen 
totaal_toegangtickets = aantal_mensen * TOEGANGTICKET_PER_PERSOON


compleet_bedrag = totaal_kosten_gameseat + totaal_toegangtickets

print(compleet_bedrag.__round__(1))


