vertaalwoordenboek = {
    'python': 'slang',
    'programma': 'code',
    'tekst': 'woord',
    'hertaling': 'vertaling',
    'machine': 'apparaat'
}

print("Beschikbare woorden om te vertalen:", ', '.join(vertaalwoordenboek))

input_tekst = input("Voer een stukje tekst in: ")

vertaalde_tekst = []
for woord in input_tekst.split():
    vertaalde_tekst.append(vertaalwoordenboek.get(woord, woord))

print("Vertaalde tekst:", ' '.join(vertaalde_tekst))



