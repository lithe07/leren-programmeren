from fruitmand02 import fruitmand

kleuren_vertaling = {
    'yellow': 'geel',
    'green': 'groen',
    'orange': 'oranje',
    'red': 'rood',
    'brown': 'bruin',
    'purple': 'paars',
    'pink': 'roze',
    'black': 'zwaart'
}

fruit_met_langste_naam = max(fruitmand, key=lambda fruit: len(fruit['name']))

vertaalde_kleur = kleuren_vertaling[fruit_met_langste_naam['color']]

print(f"Kleur: {vertaalde_kleur}, Gewicht: {fruit_met_langste_naam['weight']} gram, Naam: {fruit_met_langste_naam['name']}")
