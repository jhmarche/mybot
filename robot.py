from sensor import SENSOR
from motor import MOTOR
import pybullet as p
import pyrosim.pyrosim as pyrosim
from pyrosim.neuralNetwork import NEURAL_NETWORK


class ROBOT:
    def __init__(self):
        self.robotId = p.loadURDF("body.urdf")
        self.nn = NEURAL_NETWORK("brain.nndf")
        pyrosim.Prepare_To_Simulate(self.robotId)
        self.Prepare_To_Sense()
        self.Prepare_To_Act()

    def Prepare_To_Sense(self):
        self.sensors = {}
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)

    def Sense(self, t):
        for key, sensor in self.sensors.items():
            sensor.Get_Value(t)

    def Prepare_To_Act(self):
        self.motors = {}
        for self.jointName in pyrosim.jointNamesToIndices:
            self.motors[self.jointName] = MOTOR(self.jointName)

    def ACT(self, t):
        for key, motor in self.motors.items():
            motor.Set_Value(t, self.robotId)

    def Think(self):
        self.nn.Update()
        self.nn.Print()

