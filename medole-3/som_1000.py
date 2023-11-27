totaal = 0
getal = 50
iteratie = 1

while totaal <= 1000:
    totaal += getal
    getallenreeks = ' + '.join(map(str, range(50, getal+1)))
    print(f"{iteratie}. {getallenreeks} = {totaal}")
    getal += 1
    iteratie += 1


