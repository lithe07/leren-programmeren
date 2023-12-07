from collections import defaultdict

def maak_boodschappenlijst():
    boodschappenlijst = defaultdict(int)

    while True:
        item = input("Voer het item in (of 'stop' om te eindigen): ").strip().lower()

        if item == 'stop':
            break

        hoeveelheid = int(input("Voer de hoeveelheid in: "))

        # Controleer of het item al in de lijst staat, ongeacht de hoofdletters
        for bestaand_item in boodschappenlijst:
            if bestaand_item == item:
                item = bestaand_item
                break

        boodschappenlijst[item] += hoeveelheid

    print("\nBoodschappenlijst:")
    for item, hoeveelheid in boodschappenlijst.items():
        print(f"x{hoeveelheid} {item.capitalize()}")

if __name__ == "__main__":
    maak_boodschappenlijst()
