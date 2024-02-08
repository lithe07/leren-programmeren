def telling_elementen(getallen):
    a = {}
    for getal in getallen:
        aantalkeer = a[getal]+1 if getal in a else 1
        a[getal] = aantalkeer
    return a

lijst = [10, 16, 69, 6, 69, 5, 69, 5, 10]
elementen = telling_elementen(lijst)
for getal, aantalkeer in elementen.items():
    print(f'{getal} x {aantalkeer}')
