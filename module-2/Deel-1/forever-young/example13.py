from RobotArm import RobotArm

robotArm = RobotArm()
robotArm.randomLevel(1,7)

i = 1
while 1 > 0:
    robotArm.grab()
    color = robotArm.scan()
    if color != '':
        for x in range(i):
            robotArm.moveRight()
        robotArm.drop()
        for z in range(i):
            robotArm.moveLeft()
        i +=1
    else:
        break

robotArm.wait()