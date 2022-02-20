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
        self.world = WORLD()
        self.robot = ROBOT()
        p.setGravity(c.ZERO, c.ZERO, -9.8)
        pyrosim.Prepare_To_Simulate(self.robot)
