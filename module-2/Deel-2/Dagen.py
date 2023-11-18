WEEK_DAGEN = ('maandag', 'dinsdag', 'woensdag', 'donderdag', 'vrijdag', 'zaterdag', 'zondag')

# print('aantal dagen in de week: ')
for dag in WEEK_DAGEN:
    print(dag, end=' ')
print()

# print("aantal werk dagen: ")
for dag in WEEK_DAGEN:
    if dag.lower() not in ['zaterdag', 'zondag']:
        print(dag, end=' ')
print()


# print('weekenden: ')
for dag in WEEK_DAGEN:
    if dag.lower() in ['zaterdag', 'zondag']:
        print(dag, end=' ')
print()

# print('aantal dagen in de week omgekeerd : ')
for dag in reversed (WEEK_DAGEN):
    print(dag, end=' ')
print()

# print("aantal werk dagen omgekeerd: ")
for dag in reversed(WEEK_DAGEN):
    if dag.lower() not in ['zaterdag', 'zondag']:
        print(dag, end=' ')
print()

# print('weekenden omgekeerd: ')
for dag in reversed(WEEK_DAGEN):
    if dag.lower() in ['zaterdag', 'zondag']:
        print(dag, end=' ')
print()