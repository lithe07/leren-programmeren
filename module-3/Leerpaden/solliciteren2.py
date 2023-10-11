MAX_GEWICHT = 120
MIN_GEWICHT = 90
MAX_LENGTE = 220
MIN_LENGTE = 150

GESLACHT_MAN = "man"
GESLACHT_VROUW = "vrouw"
IN_DE_WAR = "anders"

print("---------- Sollicitatie formulier (Circusdirecteur)----------")
print("Er wordt aan u een aatal relevente vragen gesteld")
print("Gelieve die naar eer en geweten in te vullen")
print("Als blijkt dat u aan de creteria voldoet dan komt u in")
print("aanmerking voor een serius sollicitatiegesprek!")
print("Ontspan maar blijf wakker, hier komen de vragen")
print("--------------- Sucses ---------------")




print('Je kunt de vragen beantwoorden met ja / nee')
#sollicitati eisen
vrachtwagen_rijbewijs = input('Ben je in bezit van een geldige vrachtwagen rijbewijs? ')
hoed = input('Ben je in bezit van een hoge hoed? ')
gewicht = float(input('Wat is jou gewicht? '))
langte = int(input('Hoe lang ben je? '))
certificaat = input('Heeft Certificaat Overleven met gevaarlijk personeel? ')
dieren_dressuur = int(input('hoe veel jaar/jaren heb je ervaring met praktijkervaring met dieren-dressuur? '))
jongleren = int(input('hoe veel jaar ervaring heb je met jongleren? '))
acrobatiek = int(input('hoe veel jaar ervaring heb je met acrobatiek? '))
diploma_mbo = input("Bent u een bezit van een diploma MBO-4 Ondernemen? ")
ondernemer = int(input("Hoeveel ervare jaren heeft u? "))
werknemers = int(input("Met hoeveel werk nemers heeft u gewerkt? "))
geslacht = input("Wat is jou gelacht? man/vrouw/anders ")

if geslacht == "man":
    snor_lengte = input("Hoe breed is jouw snor in cm? ")    
elif geslacht == "vrouw":
    haar_lengte = input("Hoe lang is uw krulhaar in cm? ")
elif geslacht == "anders":
    glimlacht_lengte = input("Hoe breed is uw glimlach in cm? ")
 

if(vrachtwagen_rijbewijs == 'ja'
    and hoed == 'ja'
    and gewicht >= MIN_GEWICHT and gewicht <= MAX_GEWICHT
    and langte >= MIN_LENGTE and langte <= MAX_LENGTE
    and certificaat == 'ja'
    and dieren_dressuur >= 4
    and diploma_mbo == "ja" or ondernemer >= 3 and werknemers >= 5
    and snor_lengte > 10 or haar_lengte > 20 or glimlacht_lengte > 10

):
    print('Gefeliciteerd! U komt in aanmerking voor deze functie. ')
elif (
vrachtwagen_rijbewijs == 'ja'
    and hoed == 'ja'
    and gewicht >= MIN_GEWICHT and gewicht <= MAX_GEWICHT
    and langte >= MIN_LENGTE and langte <= MAX_LENGTE
    and certificaat == 'ja'
    and jongleren >= 5 or acrobatiek >= 3
    and snor_lengte > 10 or haar_lengte > 20 or glimlacht_lengte > 10

):
    print('Gefeliciteerd! U komt in aanmerking voor deze functie. ')

else:
    print('U voldoet niet aan onze strenge eisen voor de functie Circusdirecteur, Helaas het spijt ons. ')