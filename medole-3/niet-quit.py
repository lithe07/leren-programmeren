aantal_poging = 0

while True:
    antwoord = input('? ')
    aantal_poging += 1

    if antwoord.lower() == 'quit':
        break

print(f"Aantal iteraties: {aantal_poging}")
