antwoord_1 = input('is de kaas geel? ')

if antwoord_1 == 'ja':
    gaten = input('zitten er gaten in? ')
    if gaten == 'ja':
        belachelijk = input('is de kaas belachelijk duur? ')
        if belachelijk == 'ja':
            print('Emmenthaler')
        elif belachelijk == 'nee':
            print('Leerdammer')
    elif gaten == 'nee':
        steen = input('is de kaas hard als steen? ')
        if steen == 'ja':
            print('parmigiano Reggiano')
        elif steen == 'nee':
            print('Goudse kaas ')
elif antwoord_1 == 'nee':
    schimmel = input('heeft de kaas blauwe schimmel? ')
    if schimmel == "ja":
        korst_1 = input('heeft da kaas korst? ')
        if korst_1 == 'ja':
            print('Blue de ochbaron')
        elif korst_1 == 'nee':
            print('Foume dambert')
    elif schimmel == 'nee':
        korst_2 = input('Heeft de kaas korst? ')
        if korst_2 == "ja":
            print('Camembert')
        elif korst_2 == 'nee':
            print('Mozzarella')
else:
    print('ongeldige invoer')



 