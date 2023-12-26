from fruitmand import fruitmand

beschikbare_kleuern = set(fruit['color'] for fruit in fruitmand)


while True:

    gekozen_kleur = input("Kies een kleur uit de fruitmand: ")

    if gekozen_kleur in beschikbare_kleuern:
        
    

    else:
        print(f"De kleur {gekozen_kleur} zit er niet in de fruitmand")

