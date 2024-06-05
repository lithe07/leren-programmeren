from data import *

def stel_vraag(vraag, ok_antwoorden):
    while True:
        antwoord = input(vraag)
        if antwoord in ok_antwoorden:
            return antwoord
        else:
            print(ONGELDIGE_INVOER_BERICHT)


