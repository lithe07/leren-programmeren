MAX_GEWICHT = 120
MIN_GEWICHT = 90
MAX_LENGTE = 220
MIN_LENGTE = 150

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


if(
    vrachtwagen_rijbewijs == 'ja'
    and hoed == 'ja'
    and gewicht >= MIN_GEWICHT and gewicht <= MAX_GEWICHT
    and langte >= MIN_LENGTE and langte <= MAX_LENGTE
    and certificaat == 'ja'
    and (dieren_dressuur >= 4 or jongleren >= 5 or acrobatiek >= 3)

):
    print('Gefeliciteerd! U komt in aanmerking voor deze functie. ')


else:
    print('U voldoet niet aan onze strenge eisen voor de functie Circusdirecteur, Helaas het spijt ons. ')