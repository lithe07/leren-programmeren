import random

score = 0
aantal_ronden = 20

while aantal_ronden > 0:
    geheime_getal = random.randint(1, 1000)
    geraden = set()  # Om herhaalde gokken te controleren

    for _ in range(10):
        getal = int(input("Raad het getal tussen 1 en 1000: "))

        if getal in geraden:
            print("Je hebt dit getal al geraden. Probeer opnieuw.")
            continue

        geraden.add(getal)

        if getal == geheime_getal:
            print(f"Gefeliciteerd! Je hebt het juiste getal geraden. Het was inderdaad {geheime_getal}.")
            score += 1
            break
        elif abs(getal - geheime_getal) < 50:
            print("Je bent warm!")
        elif abs(getal - geheime_getal) < 20:
            print("Je bent heel warm!")

        if getal > geheime_getal:
            print("Lager")
        elif getal < geheime_getal:
            print("Hoger")

    aantal_ronden -= 1
    print(f"Score tot nu toe: {score}")

    if aantal_ronden > 0:
        doorgaan = input("Nog een getal raden? (ja/nee) ")
        if doorgaan.lower() != "ja":
            break

print(f"Einde van het spel. Jouw eindscore is: {score}")
