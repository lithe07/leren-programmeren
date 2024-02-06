from collections import Counter
import math, random

def is_lijst_leeg(getallen):
    return {"Lijst is leeg, voer getallen in.": getallen} if not getallen else None

def is_getal_numeriek(getal):
    return {"Controlle getal incorrect.": getal} if not str(getal).isnumeric() else None

def bereken_gemiddelde(getallen):
    return sum(getallen) / len(getallen)

def bereken_grootste_kleinste_eerste_getal(getallen):
    return max(getallen), min(getallen), getallen[0]

def deelbaar_door(getallen, controlegetal):
    return sorted([getal for getal in set(getallen) if getal % controlegetal == 0])

def tel_elementen(getallen):
    return dict(Counter(getallen))

def vind_posities(getallen, controlegetal):
    return [index for index, num in enumerate(getallen) if num == controlegetal]

def bereken_standaardafwijking(getallen, gemiddelde):
    verschil_kwadraat = sum((x - gemiddelde) ** 2 for x in getallen)
    variantie = verschil_kwadraat / len(getallen)
    return math.sqrt(variantie)

def shuffle_lijst(getallen):
    shuffled_lijst = getallen.copy()
    random.shuffle(shuffled_lijst)
    return shuffled_lijst

def analyseer_getallenlijst(getallen, controlegetal1, controlegetal2):
    lege_lijst_check = is_lijst_leeg(getallen)
    if lege_lijst_check:
        return lege_lijst_check

    controlegetal1_check = is_getal_numeriek(controlegetal1)
    if controlegetal1_check:
        return controlegetal1_check

    controlegetal2_check = is_getal_numeriek(controlegetal2)
    if controlegetal2_check:
        return controlegetal2_check

    aantal = len(getallen)
    gemiddelde = bereken_gemiddelde(getallen)
    grootste, kleinste, eerste = bereken_grootste_kleinste_eerste_getal(getallen)
    deelbaar1 = deelbaar_door(getallen, controlegetal1)
    deelbaar2 = deelbaar_door(getallen, controlegetal2)
    telling_elementen = tel_elementen(getallen)
    posities = vind_posities(getallen, controlegetal1)
    standaardafwijking = bereken_standaardafwijking(getallen, gemiddelde)
    geshufflede_lijst = shuffle_lijst(getallen)
    random_getal = random.choice(getallen)

    resultaten = {
        "Aantal getallen": aantal,
        "Gemiddelde": gemiddelde,
        "Grootste getal": grootste,
        "Kleinste getal": kleinste,
        "Eerste getal": eerste,
        f"Deelbaar door {controlegetal1} (op volgorde)": deelbaar1,
        f"Deelbaar door {controlegetal2} (op volgorde)": deelbaar2,
        "Telling van elementen": telling_elementen,
        f"{controlegetal1} komt voor op positie(s)": posities,
        "Standaardafwijking": standaardafwijking,
        "Geshufflede lijst": geshufflede_lijst,
        "Willekeurige getal uit de lijst": random_getal,
        f"Het verschil tussen {random_getal} & {controlegetal2}": abs(random_getal - controlegetal2),
    }

    return resultaten

# Voorbeeld van het gebruik van de functie:
getallenlijst = [16, 2, 5, 8, 12, 3, 9, 16, 5, 8, 64, 33]
controlegetal1 = 8
controlegetal2 = 3
analyse_resultaat = analyseer_getallenlijst(getallenlijst, controlegetal1, controlegetal2)
print("Analyse resultaten:")
for key, value in analyse_resultaat.items():
    print(f"{key}: {value}")
