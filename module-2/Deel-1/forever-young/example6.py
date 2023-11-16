from RobotArm import RobotArm

robotArm = RobotArm('exercise 6')


robotArm.moveRight()

for i in range(3):
    # for x in range(1):
        robotArm.grab()
        robotArm.moveLeft()
        robotArm.drop()
        robotArm.moveRight()

    # for c in range(1):
        robotArm.grab()
        robotArm.moveRight()
        robotArm.drop()
        robotArm.moveLeft()



robotArm.wait()