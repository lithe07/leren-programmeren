# # name of student: 
# # number of student:
# # purpose of program: 
# # function of program:
# # structure of program: 

# toPay = int(float(input('Amount to pay: '))* 100) #
# paid = int(float(input('Paid amount: ')) * 100) #
# change = paid - toPay #

# if change > 0: #
#   coinValue = 50 #
  
#   while change > 0 and coinValue > 0: #
#     nrCoins = change // coinValue #

#     if nrCoins > 0: #
#       print('return maximal ', nrCoins, ' coins of ', coinValue, ' cents!' ) #
#       nrCoinsReturned = int(input('How many coins of ' + str(coinValue) +  ' cents did you return? ')) #
#       change -= nrCoinsReturned * coinValue #

# # comment on code below: 
#     if coinValue == 50:
#       coinValue = 20
#     elif coinValue == 20:
#       coinValue = 10
#     elif coinValue == 10:
#       coinValue = 5
#     elif coinValue == 5:
#       coinValue = 2
#     elif coinValue == 2:
#       coinValue = 1
#     else:
#       coinValue = 0

# if change > 0: #
#   print('Change not returned: ', str(change) + ' cents')
# else:
#   print('done')




# naam student:
# studentnummer:
# doel van het programma:
# functie van het programma:
# structuur van het programma:

teBetalenBedrag = int(float(input('Te betalen bedrag in euro: ')) * 100)  # Omrekenen naar centen
betaaldBedrag = int(float(input('Betaald bedrag in euro: ')) * 100)  # Omrekenen naar centen
wisselgeld = betaaldBedrag - teBetalenBedrag

# Lijst om het aantal teruggegeven munten bij te houden
teruggegevenMunten = {
    500: 0,  # 5 euro
    200: 0,  # 2 euro
    100: 0,  # 1 euro
    50: 0,   # 50 cent
    20: 0,   # 20 cent
    10: 0,   # 10 cent
    5: 0,    # 5 cent
    2: 0,    # 2 cent
    1: 0,    # 1 cent
}

if wisselgeld > 0:
    muntWaarde = 500  # 5 euro

    while wisselgeld > 0 and muntWaarde > 0:
        if muntWaarde >= 100:  # Controleer of het een euro muntstuk is
            print('Geef maximaal', wisselgeld // 100, 'munt(en) van', muntWaarde // 100, 'euro terug!')
        else:
            print('Geef maximaal', wisselgeld // muntWaarde, 'munt(en) van', muntWaarde, 'cent terug!')

        aantalTeruggegevenMunten = int(input('Hoeveel munten van ' + str(muntWaarde // 100) + ' euro heb je teruggegeven? '))
        wisselgeld -= aantalTeruggegevenMunten * muntWaarde

        # Update het aantal teruggegeven munten
        teruggegevenMunten[muntWaarde] += aantalTeruggegevenMunten

        if muntWaarde == 500:
            muntWaarde = 200
        elif muntWaarde == 200:
            muntWaarde = 100
        elif muntWaarde == 100:
            muntWaarde = 50
        elif muntWaarde == 50:
            muntWaarde = 20
        elif muntWaarde == 20:
            muntWaarde = 10
        elif muntWaarde == 10:
            muntWaarde = 5
        elif muntWaarde == 5:
            muntWaarde = 2
        elif muntWaarde == 2:
            muntWaarde = 1
        elif muntWaarde == 1:
            muntWaarde = 0

if wisselgeld > 0:
    print('Wisselgeld niet teruggegeven: ', str(wisselgeld) + ' cent')
else:
    print('Klaar! Overzicht van teruggegeven munten:')
    for waarde, aantal in teruggegevenMunten.items():
        if waarde >= 100:
            print(f'{aantal} munt(en) van {waarde // 100} euro')
        else:
            print(f'{aantal} munt(en) van {waarde} cent')






























