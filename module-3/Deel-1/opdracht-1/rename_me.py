# Deze functie kijkt of het getal even of oneven is en antwoord met true en false:
def even_oneven(getal:int) -> bool:
    return getal % 2 == 0

# Deze functie reverse het zin 
def reverse_zin(zin:str) -> str:
    betoverde_druif = zin.split()
    doldwaze_broccoli = betoverde_druif[::-1]
    tijdmachine_pannenkoekenmix = ' '.join(doldwaze_broccoli)
    return tijdmachine_pannenkoekenmix

# Deze functie kijkt telt letters van de zin die (NIET HERHAALD ZIJN)
def herhaald_optellen(tekst:str) -> int:
    planetair_taartje = set(tekst)
    whatchamacallit = len(planetair_taartje)
    return whatchamacallit

# Deze functie telt de zin of de letters en returnt antwoord met komma getal
def optellen_met_komma(zin:str) -> float:
    wobbelwobbel = zin.split()
    
    blork = 0
    for snorkelwagen in wobbelwobbel:
        blork += len(snorkelwagen)

    bizarro_matrix = blork / len(wobbelwobbel)
    return bizarro_matrix


# Deze funcite keert het getal van 1 t/m nummer 10:
def getal_keren(getal:int, parallelle_tosti:int=10) -> None:
    for zwabber_krakeling in range(1, parallelle_tosti+1):
        laser_sandwich = zwabber_krakeling * getal
        print(f'{zwabber_krakeling} x {getal} = {laser_sandwich}')