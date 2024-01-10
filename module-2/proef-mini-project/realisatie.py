from random import shuffle

namen_lijst = []

print("Start de programma")

while True:
    naam = input("Schrijf je naam in: ")

    if naam.isalpha():
        if naam not in namen_lijst:
            namen_lijst.append(naam)

            if len(namen_lijst) >= 3:
                vraag_aantal = input("Wil je nog een naam toevoegen? Antwoord met ja/nee: ")
                if vraag_aantal.lower() == 'ja':
                    continue
                else:
                    break
        else:
            print('Je hebt deze naam al toegevoegd')
    else:
        print('Voer een geldige naam in (alleen letters toegestaan).')

shuffle(namen_lijst)
for i in range(len(namen_lijst)):
    gever = namen_lijst[i]
    ontvanger = namen_lijst[(i + 1) % len(namen_lijst)]
    print(f'{gever} trekt lootje voor {ontvanger}')

        

