from fruitmand02 import fruitmand
import random


fruit_aantal = int(input("Geef het aantal? "))

for x in range(fruit_aantal):
    fruit = random.choice(fruitmand)['name']
    print(f"{fruit}")