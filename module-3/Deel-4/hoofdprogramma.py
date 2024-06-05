# hoofdprogramma.py
from data import *
from functions import *

print(WELKOM_BERICHT)
print(MISSIE_BERICHT)

kluis = stel_vraag(KLUIS_KEUZE_BERICHT, ['rechts', 'links'])
if kluis == 'rechts':
    eind_gang = stel_vraag(DOORLOPEN_BERICHT, ['links', 'rechts'])
    if eind_gang == 'rechts':
        print(OPGEPAKT_BERICHT)
    elif eind_gang == 'links':
        print(KLUIS_BEREIKT_BERICHT)
        ontsnappings_keuze = stel_vraag(ONTSNAPPING_VRAAG_BERICHT, ['auto', 'scooter'])
        if ontsnappings_keuze == 'auto':
            auto_vraag_result = stel_vraag(AUTO_VRAAG_BERICHT, ['snelweg', 'stad'])
            if auto_vraag_result == 'snelweg':
                print(DOORRIJDEN_VERLOREN_BERICHT)
            elif auto_vraag_result == 'stad':
                print(STAD_ONTSNAPT_BERICHT)
        elif ontsnappings_keuze == 'scooter':
            scooter_vraag_result = stel_vraag(SCOOTER_VRAAG_BERICHT, ['doorrijden', 'zijstraatjes'])
            if scooter_vraag_result == 'doorrijden':
                print(DOORRIJDEN_VERLOREN_BERICHT)
            elif scooter_vraag_result == 'zijstraatjes':
                print(ZIJSTRAATJES_ONTSNAPT_BERICHT)
elif kluis == 'links':
    print(OPGEPAKT_BERICHT)