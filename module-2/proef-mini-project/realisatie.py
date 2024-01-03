import random

namen = set()
while len(namen) < 3:
    naam = input("Voer een unieke naam in: ")
    if naam not in namen:
        namen.add(naam)
    else:
        print("Deze naam is al ingevoerd. Probeer een andere naam.")

namen = list(namen)

while True:
    geschudde_namen = namen[:]
    random.shuffle(geschudde_namen)
    if all(geschudde_namen[i] != namen[i] for i in range(len(namen))):
        break

for i in range(len(namen)):
    print(f"{namen[i]} heeft het lootje van: {geschudde_namen[i]}")
