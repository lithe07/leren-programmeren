from functions import *
nummer1 = True
nummer2 = False

print("Welkom In onze Rekenmachine")
vraag = stel_vraag('A) getallen optellen\n'
                   'B) getallen aftrekken\n'
                   'C) getallen vermenigvuldigen\n'
                   'D) getallen delen\n'
                   'E) getallen ophogen\n'
                   'F) getallen verlagen\n'
                   'G) getallen verdubblen\n'
                   'H) getallen halveren\n').lower()
if vraag in ['e', 'f', 'g', 'h']:
    nummer1 = float(int(stel_vraag('welke getal')))
else:
    nummer1 = float(int(stel_vraag('welke getal')))
    nummer2 = float(int(stel_vraag(f'welke getal met {nummer1}')))
choice = actie_kiezen(vraag, nummer1, nummer2)
print(choice)

keuze = ('A) getallen optellen\n'
'B) getallen aftrekken\n'
'C) getallen vermenigvuldigen\n'
'D) getallen delen\n'
'E) getallen ophogen\n'
'F) getallen verlagen\n'
'G) getallen verdubblen\n'
'H) getallen halveren\n')

eeste_keer = True
while True:
    vraag = stel_vraag(keuze)
    if vraag == 'i':
        print('eind het programma')
        break
    elif vraag in ['e', 'f', 'g', 'h']:
        if  eeste_keer:
            nummer1 = float(int(stel_vraag('welke getal')))
        else:
            nummer1 = choice
    else:
        nummer2 = float(int(stel_vraag(f'welke getal met {choice}')))
    choice = actie_kiezen(vraag, choice, nummer2)
    print(choice)
    eeste_keer = False
    keuze += 'I) Stop'














