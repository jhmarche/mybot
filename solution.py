import numpy
import pyrosim.pyrosim as pyrosim
import random
import os
import time
import constants as c


class SOLUTION:
    def __init__(self, nextAvailableID):
        self.weights = numpy.random.rand(c.numSensorNeurons, c.numMotorNeurons)
        self.weights = self.weights * 2 - 1
        self.myID = nextAvailableID

    def Start_Simulation(self, directOrGUI):
        self.Generate_World()
        self.Generate_Body()
        self.Generate_Brain()
        os.system("python3 simulate.py " + directOrGUI + " " + str(self.myID) + " 2&>1 &")
        os.system(" start /B python3 simulate.py " + directOrGUI + str(self.myID))

    def Wait_For_Simulation_To_End(self):
        fitnessFileName = "fitness" + str(self.myID) + ".txt"
        while not os.path.exists(fitnessFileName):
            time.sleep(0.01)
        f = open("fitness" + str(self.myID) + ".txt", "r")
        my_string = f.read()
        while my_string == '':
            my_string = f.read()
            time.sleep(0.01)
        self.fitness = float(my_string)
        os.system("rm fitness" + str(self.myID) + ".txt")
        f.close()

    def Mutate(self):
        randomRow = random.randint(0, c.numSensorNeurons-1)
        randomColumn = random.randint(0, c.numMotorNeurons-1)
        self.weights[randomRow, randomColumn] = random.random() * 2 - 1

    def Set_ID(self, nextAvailableID):
        self.myID = nextAvailableID

    # function to create world
    def Generate_World(self):
        # file to store information about world
        pyrosim.Start_SDF("world.sdf")

        # creates a box
        pyrosim.Send_Cube(name="Box", pos=[-3, 3, 0.5], size=[1, 1, 1])

        # stop pyrosim
        pyrosim.End()

    # function to create body of robot
    def Generate_Body(self):
        # file to store body of robot
        pyrosim.Start_URDF("body.urdf")

        # create a Torso
        pyrosim.Send_Cube(name="Torso", pos=[0, 0, 1], size=[1, 1, 1])

        # create a joint for BackLeg and Torso
        pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso", child="BackLeg",
                           type="revolute", position=[0, -0.5, 1], jointAxis="1 0 0")

        # create a BackLeg
        pyrosim.Send_Cube(name="BackLeg", pos=[0, -0.5, 0], size=[0.2, 1, 0.2])

        # create a second joint for torso and front leg
        pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso", child="FrontLeg",
                           type="revolute", position=[0, 0.5, 1], jointAxis="1 0 0")

        # create front leg
        pyrosim.Send_Cube(name="FrontLeg", pos=[0, 0.5, 0], size=[0.2, 1, 0.2])

        # create a joint for BackLeg and Torso
        pyrosim.Send_Joint(name="Torso_LeftLeg", parent="Torso", child="LeftLeg",
                           type="revolute", position=[-0.5, 0, 1], jointAxis="0 1 0")

        # create a BackLeg
        pyrosim.Send_Cube(name="LeftLeg", pos=[-0.5, 0, 0], size=[1.0, 0.2, 0.2])

        # stop pyrosim
        pyrosim.End()

    # function to create brain of robot
    def Generate_Brain(self):
        # file to store brain of robot
        pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")

        # create a neuron for torso
        pyrosim.Send_Sensor_Neuron(name=0, linkName="Torso")

        # create a neuron for back leg
        pyrosim.Send_Sensor_Neuron(name=1, linkName="BackLeg")

        # create a neuron for front leg
        pyrosim.Send_Sensor_Neuron(name=2, linkName="FrontLeg")

        # create neuron for torso/back leg motor
        pyrosim.Send_Motor_Neuron(name=3, jointName="Torso_BackLeg")

        # create neuron for torso/front leg motor
        pyrosim.Send_Motor_Neuron(name=4, jointName="Torso_FrontLeg")

        # nested for loops that creates a synapse from each neuron to each motor
        for currentRow in range(c.numSensorNeurons):
            for currentColumn in range(c.numMotorNeurons):
                pyrosim.Send_Synapse(sourceNeuronName=currentRow, targetNeuronName=currentColumn + c.numSensorNeurons,
                                     weight=self.weights[currentRow][currentColumn])

        # stop pyrosim
        pyrosim.End()