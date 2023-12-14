boodschappenlijst = {}

while True:
    item = input("Voer het item in (of 'stop' om te eindigen): ").lower().strip()

    if item == 'stop':
        break

    hoeveelheid = int(input("Voer de hoeveelheid in: "))

    if item in boodschappenlijst:
        boodschappenlijst[item] += hoeveelheid
    else:
        boodschappenlijst[item] = hoeveelheid

print("Boodschappenlijst:")
for item, hoeveelheid in boodschappenlijst.items():
    print(f"x {hoeveelheid} {item.capitalize()}")
print('-----------------------------------------------')
