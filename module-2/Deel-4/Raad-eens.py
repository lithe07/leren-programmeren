# import random 

# score = 0 
# aantal_pogingen = 10
# aantal_ronden = 20


# while aantal_ronden > 0:
#     geheime_getal = random.randint(1, 1000)
#     while aantal_pogingen > 0:
#         getal = int(input("Raad het getal tussen 1 en 1000? "))
#         verschil = abs(geheime_getal - getal)
#         print(geheime_getal)
#         if getal == geheime_getal:
#             score += 1
#             aantal_ronden -= 1
#             aantal_pogingen -= aantal_pogingen
#             print(f"Geraden, Jouw score is {score}, Je hebt nog {aantal_ronden} ronden te gaan")

#         elif getal > geheime_getal:
#             print("Lager")
#         elif getal < geheime_getal:
#             print("Hoger")

#         aantal_pogingen -= 1

#         if verschil < 20 and getal != geheime_getal:
#             print("Jij bent heel warm!")
#         elif verschil < 50 and getal != geheime_getal:
#             print("Jij bent warm!")

#         if aantal_pogingen == 0:
#             aantal_ronden -= 1
#             print(f"Je hebt deze ronde verloren, Je hent nog {aantal_ronden} te gaan.")

#     spelen = input("Wil je nog spelen antwoord met ja/nee? ")
#     aantal_pogingen += 10
#     if spelen == 'nee':
#         print(score)
#         break
#     if aantal_ronden == 0:
#         print("Je hebt verloren.")
#     elif score == 20:
#         print("Je hebt gewonnen!")
# print("Einde programma")





import random

score = 0
rounds = 0

vraag = input("Wil je spelen? (Ja/Nee): ")

if vraag.lower() == 'ja':
    while rounds < 20:
        geheim_getal = random.randint(1, 1000)
        geraden = 10

        while geraden > 0:
            print(geheim_getal)
            raad = int(input("Raad een nummer tussen 1 en 1000: "))

            if raad == geheim_getal:
                print("Geraad!")
                score += 1
                break
            elif raad < geheim_getal:
                print("Hoger")
            else:
                print("Lager")

            verschil = abs(raad - geheim_getal)
            if verschil < 20:
                print("Je bent heel warm")
            elif verschil < 50:
                print("Je bent warm")

            geraden -= 1
            print(f"Je mag nog {geraden} keer raden")

        rounds += 1
        print("Score:", score)

        if rounds == 20:
            break

        volgende_rond = input("Raad another number? (Ja/Nee): ")
        if volgende_rond.lower() != 'ja':
            break

print("Eindscore: ", score)
