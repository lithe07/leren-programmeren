MIJN_NAAM = 'lithe'
SLB_NAAM = "jouke"

gastheer = input('wie is de gastheer? ')
gasten = 0
drank = 1
chips = 0

if (gastheer == MIJN_NAAM) or ((gasten and chips and drank) or (gastheer and drank)) and gastheer != SLB_NAAM:
    print('Start the Party')
else:
    print('geen feest')