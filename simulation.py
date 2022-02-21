from world import WORLD
from robot import ROBOT
import pybullet as p
import constants as c
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim


class SIMULATION:
    def __init__(self):
        self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0, 0, -9.8)
        self.world = WORLD()
        self.robot = ROBOT()

    def __del__(self):
        p.disconnect()

    def Run(self):
        for t in range(c.ITERATIONS):
            print(t)
            p.stepSimulation()
            self.robot.Sense(t)
            self.robot.ACT(t)
            #     pyrosim.Set_Motor_For_Joint(
            #         bodyIndex=robotId,
            #         jointName="Torso_BackLeg",
            #         controlMode=p.POSITION_CONTROL,
            #         targetPosition=backLegTargetAngles[i],
            #         maxForce=c.TEN
            #     )
            #     pyrosim.Set_Motor_For_Joint(
            #         bodyIndex=robotId,
            #         jointName="Torso_FrontLeg",
            #         controlMode=p.POSITION_CONTROL,
            #         targetPosition=frontLegTargetAngles[i],
            #         maxForce=c.TEN
            #     )
            time.sleep(1/60)
