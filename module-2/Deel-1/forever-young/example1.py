from RobotArm import RobotArm

robotArm = RobotArm('exercise 1')

for i in range(1):
    robotArm.moveRight()
    robotArm.grab()
    robotArm.moveLeft()
    robotArm.drop()


robotArm.wait()