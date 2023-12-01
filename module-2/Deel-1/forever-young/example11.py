from RobotArm import RobotArm
robotArm = RobotArm('exercise 11')


beweging = 9

for a in range(8):
    robotArm.moveRight()

for i in range(beweging - i):
    robotArm.grab()
    color = robotArm.scan()
    if color == 'white':
        robotArm.moveRight()
        robotArm.drop()
        robotArm.moveLeft()
        robotArm.moveLeft()
    else:
        robotArm.drop(), robotArm.moveLeft()



robotArm.wait()
 
 
