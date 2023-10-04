aantal_mensen = int(input("Hoeveel mensen gaan mee? "))

toegangticket_per_persoon = int(float(input("Hoeveel kost de toeganticket? ")) * 100)
gameseat_per_5_minuut = int(float(input("Hoeveel kost per 5 minuut? ")) * 100)
tijd_gameseat_minuten = int(input("Hoeveel minuten willen jullie spelen? "))
PERIODE = 5

totaal_kosten_gameseat = ((tijd_gameseat_minuten / PERIODE) * gameseat_per_5_minuut) * aantal_mensen 
totaal_toegangtickets = aantal_mensen * toegangticket_per_persoon


compleet_bedrag = totaal_kosten_gameseat + totaal_toegangtickets
print(f"Dit geweldige dagje-uit met {aantal_mensen} mensen in de speelhal met {tijd_gameseat_minuten} minuten VR kost je maar {compleet_bedrag} euro ")


