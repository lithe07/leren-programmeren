from fruitmand import fruitmand

kleuren_vertaling = {
    'yellow': 'geel',
    'green': 'groen',
    'orange': 'oranje',
    'red': 'rood',
    'brown': 'bruin'
}

# Zoek het fruit met de langste naam
fruit_met_langste_naam = max(fruitmand, key=lambda fruit: len(fruit['name']))

# Vertaal de kleur
vertaalde_kleur = kleuren_vertaling[fruit_met_langste_naam['color']]

# Print de details
print(f"Kleur: {vertaalde_kleur}, Gewicht: {fruit_met_langste_naam['weight']} gram, Naam: {fruit_met_langste_naam['name']}")
