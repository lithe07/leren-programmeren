MIJN_NAAM = 'lithe'
SLB_NAAM = "jouke"

GASTEN_VAN_4 = 4
GASTEN_VAN_20 = 20


gastheer = input('wie is de gastheer? ')
gasten = int(input("Hoeveel gasten zijn er? "))
drank = 1
chips = 0

if (gastheer == MIJN_NAAM) or ((gasten and chips and drank) or (gastheer and drank)) and gastheer != SLB_NAAM:
    print('Start the Party')
else:
    print('geen feest')