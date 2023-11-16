getal = int(input("Voer een getal in: "))
 
print(f"Tafel van {getal}:")
for i in range(11, 21):
    resultaat = getal * i
    print(f"{getal} x {i} = {resultaat}")
