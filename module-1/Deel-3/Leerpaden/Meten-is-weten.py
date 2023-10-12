a = int(input("voer het eerste getal in. "))
b = int(input("voer het tweede getal in. "))

MIN = 0
MAX = 0


# input en if-statement
if a > b:
    MAX = a
    print(f"a is het grootste getal. {MAX}")
# elif-statement
elif a < b:
    MIN = a
    print(f"a is het kleinste getal. {MIN}")
# else-statement 
else:
    print("a is evengelijk aan b")

# Min en Max
print(f"Het minimum getal is: {MIN}")
print(f"Het maximum getal is: {MAX}")
