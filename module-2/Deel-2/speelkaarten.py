import random

kaarten = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Boer', 'Vrouw', 'Heer', 'Aas']
soorten = ['Harten', 'Ruiten', 'Klaveren', 'Schoppen']

deck = []
for kaart in kaarten:
    for soort in soorten:
        huidige_kaart = f'{kaart} {soort}'
        deck.append(huidige_kaart)

random.shuffle(deck)

for i, kaart in enumerate(deck[:7]):
    print(f'Kaart {i+1}: {kaart}')

print(f'Rest van de kaarten in het kaartspel ({len(deck)-7} overgebleven):')
print(deck[7:])
 