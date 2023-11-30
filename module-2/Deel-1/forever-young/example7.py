from RobotArm import RobotArm

robotArm = RobotArm('exercise 7')

count = 0

while count <= 30:  # Pas het aantal herhalingen aan zoals nodig
    robotArm.moveRight()
    robotArm.grab()
    robotArm.moveLeft()
    robotArm.drop()
    count += 1

    # Voer de extra beweging uit na de eerste set van 6 blokken
    if count % 6 == 0:
        robotArm.moveRight()
        robotArm.moveRight()
robotArm.wait()

