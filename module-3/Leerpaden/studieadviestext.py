ALTIJD = 0
VAAK = 1
REGELMATIG = 2
SOMS = 3
NOOIT = 4
GEMIDDELD = 3
STUDIEDOKTER_TITEL = '''

*********************** STUDIEADVIES ***********************
Ik ga jou helpen met jouw opleiding. Jij krijgt een aantal stellingen te zien.
Voor elke stelling moet je zeggen hoeveel dat bij jou voorkomt. Je kunt steeds
antwoorden: 0 is 'altijd'; 1 is 'vaak'; 2 is 'regelmatig'; 3 is 'soms'; 4 is 'nooit'.
Het is belangrijk om eerlijk te zijn. Op basis van jouw antwoorden krijg je advies.
'''

OPTIES = "Kies 0: altijd; 1: vaak; 2: regelmatig; 3: soms; 4: nooit"
AANTAL_WEKEN_VRAAG = 'Hoeveel weken ben je al bezig met de opleiding?'
COMPETENTIE_STELLING_1 = 'Ik voel stress of blokkades bij het maken van programmeeropdrachten.'
COMPETENTIE_STELLING_2 = 'Ik stel programmeeropdrachten en -uitdagingen uit.'
COMPETENTIE_STELLING_3 = 'Ik denk dat ik geen talent heb voor de opleiding.'
COMPETENTIE_STELLING_4 = 'Ik vermijd assessments (CJV) en feedback van kritische docenten. '
COMPETENTIE_STELLING_5 = 'Ik vergelijk mezelf met anderen die beter lijken te zijn.'
COMPETENTIE_STELLING_6 = 'Ik voel geen interesse in nieuwe programmeertechnieken.'
COMPETENTIE_STELLING_7 = 'Ik kopieer code van anderen en lever dat in alsof het helemaal van mij is.'
ZORGELIJK = 2
TWIJFELACHTIG = 3
COMPETENTIE_ADVIES_TITEL = '''


*********************** STUDIEADVIES ***********************'''

COMPETENTIE_ADVIES_ZORGELIJK = '''
Het lijkt erop dat je nog weinig zelfvertrouwen, voldoening en plezier ervaart
in het leren programmeren. Er zijn altijd mogelijkheden om je te helpen de draad
op te pakken met de opleiding. Praat met jouw SLB-er over extra begeleiding en oefeningen.
'''
COMPETENTIE_ADVIES_TWIJFELACHTIG = '''
Het lijkt erop dat je af en toe weinig zelfvertrouwen, voldoening of plezier ervaart
in het leren programmeren. Houd je zelfvertrouwen en motivatie in de gaten!
'''
COMPETENTIE_ADVIES_GERUSTSTELLEND = '''
Het lijkt erop dat je voldoende zelfvertrouwen, voldoening en plezier ervaart in
het leren programmeren. Mocht het een keer minder gaan, maak je geen zorgen. Have fun!
'''

print(STUDIEDOKTER_TITEL)

print(OPTIES)

# Ask about the number of weeks studied
aantal_weken_vraag = int(input(AANTAL_WEKEN_VRAAG))

# Conditionally ask questions 6 and 7 based on the number of weeks studied
if aantal_weken_vraag >= 10:
    competentie_stelling_6 = int(input(COMPETENTIE_STELLING_6))
    competentie_stelling_7 = int(input(COMPETENTIE_STELLING_7))
else:
    competentie_stelling_6 = competentie_stelling_7 = NOOIT  # Set to a default value if not asked

# Ask other questions
competentie_stelling_1 = int(input(COMPETENTIE_STELLING_1))
competentie_stelling_2 = int(input(COMPETENTIE_STELLING_2))
competentie_stelling_3 = int(input(COMPETENTIE_STELLING_3))
competentie_stelling_4 = int(input(COMPETENTIE_STELLING_4))
competentie_stelling_5 = int(input(COMPETENTIE_STELLING_5))


scoor = (
    (competentie_stelling_1 + competentie_stelling_2 + competentie_stelling_3 + competentie_stelling_4
    + competentie_stelling_5 + competentie_stelling_6 + competentie_stelling_7) / GEMIDDELD
)

# Provide advice based on the score
if scoor <= ZORGELIJK:
    print(COMPETENTIE_ADVIES_ZORGELIJK)

elif scoor <= TWIJFELACHTIG:
    print(COMPETENTIE_ADVIES_TWIJFELACHTIG)
else:
    print(COMPETENTIE_ADVIES_GERUSTSTELLEND)


# ... (je bestaande code blijft hier)

# Tellen van het aantal antwoorden 'altijd', 'vaak' en 'regelmatig'
aantal_altijd = sum(answer <= VAAK for answer in [competentie_stelling_1, competentie_stelling_2, competentie_stelling_3, competentie_stelling_4, competentie_stelling_5, competentie_stelling_6, competentie_stelling_7])
aantal_vaak = sum(answer == VAAK for answer in [competentie_stelling_1, competentie_stelling_2, competentie_stelling_3, competentie_stelling_4, competentie_stelling_5, competentie_stelling_6, competentie_stelling_7])
aantal_regelmatig = sum(answer == REGELMATIG for answer in [competentie_stelling_1, competentie_stelling_2, competentie_stelling_3, competentie_stelling_4, competentie_stelling_5, competentie_stelling_6, competentie_stelling_7])

# Berekenen van de gemiddelde score
gemiddelde_score = (
    competentie_stelling_1 + competentie_stelling_2 + competentie_stelling_3 +
    competentie_stelling_4 + competentie_stelling_5 + competentie_stelling_6 + competentie_stelling_7
) / GEMIDDELD

# Verbeterd advies gebaseerd op de gegeven criteria
if gemiddelde_score <= 2 or aantal_altijd + aantal_vaak > 3.5:
    advies = COMPETENTIE_ADVIES_ZORGELIJK
elif gemiddelde_score <= 3 or aantal_altijd + aantal_vaak + aantal_regelmatig > 3.5:
    advies = COMPETENTIE_ADVIES_TWIJFELACHTIG
else:
    advies = COMPETENTIE_ADVIES_GERUSTSTELLEND

# Tonen van het verbeterde advies
print(f'\nVerbeterd Advies: {advies}\n')