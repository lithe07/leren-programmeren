import random

aantal_kleuren = ('oranje', 'blauw', 'groen', 'bruin')

aantal_mms_toevoegen = int(input("Hoeveel M&M's wil je aan de zak toevoegen? "))

mms_zak = []

for _ in range(aantal_mms_toevoegen):
    kleur = random.choice(aantal_kleuren)
    mms_zak.append(kleur)

print(f"De gevulde M&M's zak: {mms_zak}")
