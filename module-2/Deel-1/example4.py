from RobotArm import RobotArm
robotArm = RobotArm('exercise 4')

for eri in range(4):
    print(eri)
    robotArm.grab()
    for eri in range(2):
        robotArm.moveRight()
    robotArm.drop()

    for eri in range(2):
        robotArm.moveLeft()

robotArm.grab()
robotArm.moveRight()
robotArm.drop()


for i in range(1):
    robotArm.moveRight()
for i in range(4):
    robotArm.grab()
    robotArm.moveLeft()
    robotArm.drop()
    robotArm.moveRight()

robotArm.wait()


