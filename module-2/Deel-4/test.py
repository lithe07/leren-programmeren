PRIJS_COLA = 1.80
PRIJS_BIER = 2.40
PRIJS_CHAMPAGNE = 12.30

DRANKJES = ('cola', 'bier', 'champagne')
VIP_LIST = ('jeroen', 'jouke', 'rudi')

print("Start programma")
leeftijd = int(input("Hoe oud ben je? "))
if leeftijd > 18:
    naam = input('Wat is je naam? ')
    if naam in VIP_LIST:
        if leeftijd >= 21:
            bandje = 'blauw'
        else: 
            bandje = 'rood'
        print(f'Je krijgt van mij een {bandje} bandje')
    else:
        if leeftijd >= 21:
            print("Je krijgt van mij een stempel")
    drank = input("Wat wil je drinken? ")
    if (drank == 'cola' and naam in VIP_LIST) or (drank == 'bier' and (naam in VIP_LIST and leeftijd >= 21)):
        print("Alstublieft complimenten van het huis ")
    elif (drank == 'cola' and naam not in VIP_LIST) or (drank == 'bier' and leeftijd >= 21) or (drank == 'champagne' and naam in VIP_LIST and leeftijd >= 21):
        if drank == 'cola':
            prijs = PRIJS_COLA
        elif drank == 'bier':
            prijs = PRIJS_BIER
        else:
            prijs = PRIJS_CHAMPAGNE
        print(f'Alsjeblieft je {drank} dat is dan ${prijs}')

    elif drank == 'bier' or drank == 'champagne' and leeftijd < 21:
        print('Sorry je mag geen alcohol bestellen onder de 21')
        leeftijd_berkenen = 21 - leeftijd
        print(f'probeer over {leeftijd_berkenen} jaar nog eens')

    elif drank == 'champagne' and naam not in VIP_LIST:
        print("Sorry alleen vips mogen champagne bestellen")
    else:
        print('Sorry geen ideen wat je bedoeld, hier een glasje water')
else:
    print("Sorry je mag niet naar binnen")
    leeftijd_berkenen = 19 -leeftijd
    print(f"Probeer het over in {leeftijd_berkenen} jaar nog eens")
print('Eind programma')


