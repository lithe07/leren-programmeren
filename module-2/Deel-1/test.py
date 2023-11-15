tekst = 'Dit is tekst'  #eenvouding voorbeeld van een verzameling van karakters
tekst_2 = 'a'

for x in (0, 1, 2, 3): 
    print(tekst[x])

for x in range(len(tekst)): # dit is de manier om net zo vaak code uit te voeren als dat je vooraf wilt weten 
    pritn(tekst[x])

for x in range(4):
    print('je bent aardig ')


for c in tekst: # de c verandert per iteratie in het karakter wat dan aan de beurt is. Hij begint bij index 0 
    print(c)



tekst_3 = 'Abba was erg populier in de jaren 70'

test  = tekst_3.lower().count('a')

print(f"Het aantal keer dat de letter 'a' voorkomt is: {test}")
