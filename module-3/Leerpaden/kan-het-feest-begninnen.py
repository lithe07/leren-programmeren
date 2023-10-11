gastheer = True
gasten = False
drank = False
chips = False

if (gasten and chips and drank) or (gastheer and drank) or gastheer or gasten: 
    print('Start the Party')
else:
    print('No Party')
