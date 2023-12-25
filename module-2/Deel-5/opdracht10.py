from fruitmand import fruitmand

gesorteerde_fruitmand = sorted(fruitmand, key=lambda fruit: fruit['weight'], reverse=True)

for fruit in gesorteerde_fruitmand:
    gewicht_in_kg = fruit['weight'] / 1000  
    print(f"{fruit['name']} - {gewicht_in_kg} kg")
