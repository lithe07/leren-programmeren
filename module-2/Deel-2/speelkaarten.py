import random

kaarten = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Boer', 'Vrouw', 'Heer', 'Aas']
soorten = ['Harten', 'Ruiten', 'Klaveren', 'Schoppen']
jokers = ['joker', 'joker']

deck = []

for kaart in kaarten:
    for soort in soorten:
        huidige_kaart = f'{kaart} {soort}'
        deck.append(huidige_kaart)

deck.extend(jokers)
random.shuffle(deck)

for _ in range(7):
    print(deck.pop(0))
print(len(deck))