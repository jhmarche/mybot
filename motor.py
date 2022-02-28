import constants as c
import numpy
import pyrosim.pyrosim as pyrosim
import pybullet as p


class MOTOR:
    def __init__(self, jointName):
        self.jointName = jointName
        self.Prepare_To_Act()

    def Prepare_To_Act(self):
        self.amplitude = c.AMPLITUDE
        self.frequency = c.FREQUENCY
        self.offset = c.OFFSET
        self.motorValues = numpy.linspace(c.OFFSET, c.TWO_PI, c.ITERATIONS)
        if self.jointName == "Torso_FrontLeg":
            self.frequency = c.FREQUENCY / 2

        for x in range(len(self.motorValues)):
            self.motorValues[x] = self.amplitude * numpy.sin(self.frequency *
                                                             self.motorValues[x] + self.offset)

    def Set_Value(self, desiredAngle, robotId):
        pyrosim.Set_Motor_For_Joint(
            bodyIndex=robotId,
            jointName=self.jointName,
            controlMode=p.POSITION_CONTROL,
            targetPosition=desiredAngle,
            maxForce=c.TEN
        )

    def Save_Values(self):
        numpy.save("../mybot/data/motorValues.npy", self.motorValues)
