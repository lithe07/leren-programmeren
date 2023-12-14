import random

def raden_spel():
    geheime_getal = random.randint(1, 1000)
    score = 0
    max_ronden = 20

    for ronde in range(1, max_ronden + 1):
        geraden_getal = int(input(f"Ronde {ronde}: Raad een getal tussen 1 en 1000: "))

        verschil = abs(geraden_getal - geheime_getal)

        if geraden_getal == geheime_getal:
            print("Gefeliciteerd, je hebt het juiste getal geraden!")
            score += 1
        else:
            if verschil < 20:
                print("Je bent heel warm")
            elif verschil < 50:
                print("Je bent warm")
            else:
                print("Hoger" if geraden_getal < geheime_getal else "Lager")
                print(f"Het juiste getal was: {geheime_getal}")

        print(f"Huidige score: {score}")

        if ronde == max_ronden or input("Nog een getal raden? (ja/nee): ").lower() != 'ja':
            break

    print(f"Eindscore: {score}")

if __name__ == "__main__":
    raden_spel()
