boodschappenlijst = {}

while True:
    item = input("Voer het item in (of 'stop' om te eindigen): ")

    if item == 'stop':
        break

    hoeveelheid = int(input("Voer de hoeveelheid in: "))

    # Controleer of het item al in de lijst staat, ongeacht de hoofdletters
    for bestaand_item in boodschappenlijst:
        if bestaand_item == item:
            item = bestaand_item
            break

    if item in boodschappenlijst:
        boodschappenlijst[item] += hoeveelheid
    else:
        boodschappenlijst[item] = hoeveelheid

print("Boodschappenlijst:")
for item, hoeveelheid in boodschappenlijst.items():
    print(f"x {hoeveelheid} {item.capitalize()}")
print('-----------------------------------------------')
