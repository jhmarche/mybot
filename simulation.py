from world import WORLD
from robot import ROBOT
import pybullet as p
import constants as c
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim


class SIMULATION:
    def __init__(self, directOrGUI):
        if directOrGUI == "DIRECT":
            self.physicsClient = p.connect(p.DIRECT)
        else:
            self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0, 0, -9.8)
        self.world = WORLD()
        self.robot = ROBOT()
        self.directOrGui = directOrGUI

    def __del__(self):
        p.disconnect()

    def Run(self):
        for t in range(c.ITERATIONS):
            p.stepSimulation()
            self.robot.Sense(t)
            self.robot.Think()
            self.robot.ACT()
            if self.directOrGui == "GUI":
                time.sleep(1/60)

    def Get_Fitness(self):
        self.robot.Get_Fitness()
