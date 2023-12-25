from fruitmand02 import fruitmand02

watermeloen = {
    'name' : 'watermeloen',
    'weight' : 3500,
    'color' : 'blue',
    'round' : True
}
fruitmand.append(watermeloen)

totaal_weight = 0

for fruit in fruitmand:
    totaal_weight += fruit['weight']

print(totaal_weight)
