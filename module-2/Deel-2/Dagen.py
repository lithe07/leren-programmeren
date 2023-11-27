WEEK_DAGEN = ('maandag', 'dinsdag', 'woensdag', 'donderdag', 'vrijdag', 'zaterdag', 'zondag')


for dag in WEEK_DAGEN:
    print(dag, end=' ')
print()


for dag in WEEK_DAGEN[4::-1]:
    # if dag.lower() not in ['zaterdag', 'zondag']:
    #     print(dag, end=' ')
    print(dag)



for dag in WEEK_DAGEN:
    if dag.lower() in ['zaterdag', 'zondag']:
        print(dag, end=' ')
print()


for dag in reversed (WEEK_DAGEN):
    print(dag, end=' ')
print()


for dag in reversed(WEEK_DAGEN):
    if dag.lower() not in ['zaterdag', 'zondag']:
        print(dag, end=' ')
print()


for dag in reversed(WEEK_DAGEN):
    if dag.lower() in ['zaterdag', 'zondag']:
        print(dag, end=' ')
print()