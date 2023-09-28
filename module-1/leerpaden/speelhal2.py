AANTAL_MENSEN = 4

TOEGANGTICKET_PER_PERSOON = 7.45
GAMESEAT_PER_5_MINUUT = 0.37
TIJD_GAMESEAT_MINUTEN = 45


totaal_kosten_gameseat = ((TIJD_GAMESEAT_MINUTEN / 5) * GAMESEAT_PER_5_MINUUT) * AANTAL_MENSEN 

totaal_toegangtickets = AANTAL_MENSEN * TOEGANGTICKET_PER_PERSOON


compleet_bedrag = totaal_kosten_gameseat + totaal_toegangtickets

print(f"Dit geweldige dagje-uit met {AANTAL_MENSEN} mensen in de speelhal met {TIJD_GAMESEAT_MINUTEN} minuten VR kost je maar {compleet_bedrag.__round__(1)} euro ")


