def compare_numbers(nr1: int, nr2: int) -> str:
    if nr1 == nr2:
        return 'Beide getallen zijn even groot'
    elif nr1 > nr2:
        return f'Maximum: {nr1} en minimum: {nr2}'
    else:
        return f'Maximum: {nr2} en minimum: {nr1}'


nr1 = int(input("voer het eerste getal in. "))
nr2 = int(input("voer het tweede getal in. "))

MIN = 0
MAX = 0


# input en if-statement
if nr1 > nr2:
    MAX = nr1
    print(f"Maximum: {nr1} en minimum: {nr2}")
# elif-statement
elif nr1 < nr2:
    MIN = nr1
    print(f"Maximum: {nr2} en minimum: {nr1}")
# else-statement 
else:
    print(f"Biede getallen zijn even groot")
