from fruitmand02 import fruitmand

kleuren_in_fruitmand = []
for fruit in fruitmand:
    if fruit["color"] not in kleuren_in_fruitmand:
        kleuren_in_fruitmand.append(fruit["color"])

while True:
    gekozen_kleur = input("Kies een kleur uit de fruitmand: ").lower()

    if gekozen_kleur in kleuren_in_fruitmand:
        print("Je hebt gekozen voor de kleur", gekozen_kleur)
        break
    else:
        print(f"De gekozen kelur {gekozen_kleur } zit er niet in de fruitmand")

aantal_ronde = 0
aantal_niet_ronde = 0


for fruit in fruitmand:
    if fruit["color"] ==  gekozen_kleur:
        if fruit["round"]:
            aantal_ronde += 1
        else:
            aantal_niet_ronde += 1


if aantal_ronde > aantal_niet_ronde:
    verschil = aantal_ronde - aantal_niet_ronde
    print(f"Er zijn {verschil} meer ronde vruchten dan niet ronde vruchten in de kleur {gekozen_kleur}")
elif aantal_ronde < aantal_niet_ronde:
    verschil = aantal_niet_ronde - aantal_ronde
    print(f"Er zijn {verschil} minder ronde vruchten dan niet ronde vruchten in de kleur {gekozen_kleur}")
else:
    print(f"Er zijn {aantal_ronde} ronde vruchten en {aantal_niet_ronde} niet ronde vruchten in de kleur {gekozen_kleur}")