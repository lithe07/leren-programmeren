from random import shuffle
import time
 
def voeg_naam_toe(namen_lijst, cadeau_wensen):
    while True:
        naam = input("Schrijf je naam in: ")
 
        if naam.isalpha():
            if naam not in namen_lijst:
                namen_lijst.append(naam)
                wensen = []
                print(f"Voer 3 cadeauwensen in voor {naam}:")
                for i in range(3):
                    wens = input(f"Voer cadeauwens {i+1} in: ")
                    wensen.append(wens)
                cadeau_wensen[naam] = wensen
               
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
 
def trek_lootjes(namen_lijst):
    lootjes_dict = {}
 
    for i in range(len(namen_lijst)):
        gever = namen_lijst[i]
        ontvanger = namen_lijst[(i + 1) % len(namen_lijst)]
        lootjes_dict[gever] = ontvanger
 
    return lootjes_dict
 
def toon_lootje(lootjes_dict, cadeau_wensen):
    while True:
        vraag_naam = input("Voer een naam in om het bijbehorende lootje en cadeauwensen te zien (typ 'stop' om te stoppen): ")
        if vraag_naam.lower() == 'stop':
            break
        elif vraag_naam in lootjes_dict:
            print(f'{vraag_naam} trekt lootje voor {lootjes_dict[vraag_naam]}')
            print(f'Cadeauwensen van {vraag_naam}: {", ".join(cadeau_wensen[vraag_naam])}')
            time.sleep(2)
        else:
            print('Ongeldige naam, probeer opnieuw.')
 
namen_lijst = []
cadeau_wensen = {}
print("Start de programma")
voeg_naam_toe(namen_lijst, cadeau_wensen)
shuffle(namen_lijst)
lootjes_dict = trek_lootjes(namen_lijst)
print("Nu zijn de lootjes geheim getrokken.")
toon_lootje(lootjes_dict, cadeau_wensen)
print("Einde programma")
 