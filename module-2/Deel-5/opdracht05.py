from fruitmand import fruitmand

# fruitmand.reverse()
# for fruit in fruitmand:
#     print(fruit['name'])

for fruit in fruitmand:
    fruit['name'] = fruit['name'][::-1]
    print(fruit['name'])
