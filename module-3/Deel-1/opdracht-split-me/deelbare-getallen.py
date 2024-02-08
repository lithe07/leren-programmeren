def filter_deelbaar(getallen, controlegetal): 
    deelbaar1 = []
    posities = []
    for index, getal in enumerate(getallen):
        if getal % controlegetal == 0:
            deelbaar1.append(getal)
        if getal == controlegetal:
            posities.append(index)
    deelbaar1 = sorted(deelbaar1)
    komtvoor = controlegetal in getallen
    return deelbaar1, komtvoor, posities

getallenlijst = [16, 2, 5, 8, 12, 3, 9, 16, 5, 8, 64, 33]
controlegetal = 16
test_getal, komtvoor, posities = filter_deelbaar(getallenlijst, controlegetal)
print(test_getal)
print(f'{controlegetal}  komt voor: {komtvoor}')
print(f'Dat is de positie van de gekozen nummer {posities}')

controlegetal = 5
test_getal, komtvoor, posities = filter_deelbaar(getallenlijst, controlegetal)
print(test_getal)
print(f'{controlegetal}  komt voor: {komtvoor}')
print(f'Dat is de positie van de gekozen nummer {posities}')