import random

def raden_spel():
    geheime_getal = random.randint(1, 1000)
    score = 0
    max_pogingen = 10
    max_ronden = 20

    for ronde in range(1, max_ronden + 1):
        print(f"\nRonde {ronde}:")
        pogingen_over = max_pogingen

        while pogingen_over > 0:
            geraden_getal = int(input(f"Poging {max_pogingen - pogingen_over + 1}/{max_pogingen}: Raad een getal tussen 1 en 1000: "))
            pogingen_over -= 1

            verschil = abs(geraden_getal - geheime_getal)

            if geraden_getal == geheime_getal:
                print("Gefeliciteerd, je hebt het juiste getal geraden!")
                score += 1
                break
            else:
                if verschil < 20:
                    print("Je bent heel warm")
                elif verschil < 50:
                    print("Je bent warm")
                else:
                    print("Hoger" if geraden_getal < geheime_getal else "Lager")

                if pogingen_over > 0:
                    print(f"Je hebt nog {pogingen_over} {'pogingen' if pogingen_over > 1 else 'poging'} over.")
                else:
                    print(f"Helaas, je hebt geen pogingen meer over. Het juiste getal was: {geheime_getal}")

        print(f"Huidige score: {score}")

        if ronde == max_ronden or input("Nog een ronde spelen? (ja/nee): ").lower() != 'ja':
            break

    print(f"Eindscore: {score}")

if __name__ == "__main__":
    raden_spel()
