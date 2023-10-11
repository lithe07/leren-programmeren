MIJN_NAAM = 'lithe'
SLB_NAAM = 'jouke'

 
gastheer = input('Wie is de gastheer? ')
gasten = False
drank = False
chips = False

# print((gasten and chips and drank) or (gastheer > "" and drank))
if (gastheer == MIJN_NAAM) or ((gasten and chips and drank) or (gastheer and drank)) and gastheer != SLB_NAAM:
    print('Start the Party')
else:
    print('No party')