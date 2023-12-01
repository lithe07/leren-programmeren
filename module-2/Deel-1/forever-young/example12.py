from RobotArm import RobotArm
robotArm = RobotArm('exercise 12')

beweging = 9

for i in range(9):
    robotArm.grab()
    color = robotArm.scan()
    if color == 'red':
        for x in range(beweging - i):
            robotArm.moveRight()
        robotArm.drop()
        i += 1
        for a in range(beweging - i):
            robotArm.moveLeft()
    else:
        robotArm.drop()
        robotArm.moveRight()

robotArm.wait()