# from fruitmand02 import fruitmand

# gesorteerde_fruitmand = sorted(fruitmand, key=lambda fruit: fruit['weight'], reverse=True)

# for fruit in gesorteerde_fruitmand:
#     gewicht_in_kg = fruit['weight'] / 1000  
#     print(f"{fruit['name']} - {gewicht_in_kg} kg")


from fruitmand02 import fruitmand

# Functie om het gewicht uit een fruit dictionary te halen
def gewicht_van_fruit(fruit):
    return fruit['weight']

# Sorteer de fruitmand op gewicht in aflopende volgorde
gesorteerde_fruitmand = sorted(fruitmand, key=gewicht_van_fruit, reverse=True)

# Loop door de gesorteerde lijst en print de informatie
for fruit in gesorteerde_fruitmand:
    gewicht_in_kg = fruit['weight'] / 1000
    print(f"{fruit['name']} - {gewicht_in_kg} kg")
