
PRIJS_COLA = 1.80
PRIJS_BIER = 2.40
PRIJS_CHAMPAGNE = 12.30

DRANKJES = ('cola', 'bier', 'champagne')
VIP_LIST = ('jeroen', 'jouke', 'rudi')
prijs = 0


#bouw hieronder de floowchart na
print("Start programma")
leeftijd = int(input("Hoe oud ben je? "))
if leeftijd > 18:
    naam = input("Wat is je naam? ")
    if naam in VIP_LIST:
        if leeftijd >= 21:
            bandje = 'baluw'
        else:
            bandje = 'rood'
        print(f"Je krijgt van mij een {bandje} bandje")
    else:
        if leeftijd >= 21:
            print("Je krijgt van mij een stempel")
        else:
            print("Je krijgt van mij geen stempel")     # Hier moeten we op terug 
    drank = input("wat wil je drinken? ")
    if drank in DRANKJES[0]:
        if naam  in VIP_LIST:
            drank = DRANKJES[0]
        else:
            prijs = PRIJS_COLA
    else:
        if drank in DRANKJES[1] and leeftijd >= 21:
            drank = DRANKJES[1]
        else:
            prijs = PRIJS_BIER
            print(f"Alstublieft je {drank} dat is dan ${prijs}")
        print('Alstublieft complimenten van het huis')
          




    # elif drank in DRANKJES[1]:
    #     if naam in VIP_LIST or leeftijd >= 21:
    #         drank = 'bier'
    #     else:
    #         prijs = PRIJS_BIER
    #     print('Alstublieft complimenten van het huis')
    # elif drank in DRANKJES[2]:
    #     if naam in VIP_LIST and leeftijd >= 21:
    #         drank = 'champagne'
    #         prijs = PRIJS_CHAMPAGNE
    #     else:
    #         print('Sorry alleen vips mogen champagne bestellen')
    #     print(f"Alstublieft je {drank} dat is dan ${prijs}")
    # else:
    #     print('Sorry geen idee wat je bedoeld, hier een glasje water')