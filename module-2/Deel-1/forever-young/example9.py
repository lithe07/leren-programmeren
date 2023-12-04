from RobotArm import RobotArm
 
robotArm = RobotArm('exercise 9')

for  aantalblokjes in range(1, 5): #stapel`
    for x in range(aantalblokjes):
        for _ in range(aantalblokjes):
            robotArm.grab()
            for a in range(5): robotArm.moveRight()
            robotArm.drop()
            for b in range(4): robotArm.moveLeft()
            if x < aantalblokjes - 1:
                robotArm.moveLeft()

robotArm.wait()


#  bij opdracht 13 robotarm moet de kleur scannen of er geen kleur is dat betekent geen grab


