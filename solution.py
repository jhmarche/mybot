import numpy
import pyrosim.pyrosim as pyrosim
import random
import os
import time


class SOLUTION:
    def __init__(self, nextAvailableID):
        self.weights = numpy.random.rand(3, 2)
        self.weights = self.weights * 2 - 1
        self.myID = nextAvailableID

    def Start_Simulation(self, directOrGUI):
        self.Generate_World()
        self.Generate_Body()
        self.Generate_Brain()
        os.system("python3 simulate.py " + directOrGUI + " " + str(self.myID) + " &")
        os.system(" start /B python3 simulate.py " + directOrGUI + str(self.myID))

    def Wait_For_Simulation_To_End(self):
        fitnessFileName = "fitness" + str(self.myID) + ".txt"
        while not os.path.exists(fitnessFileName):
            time.sleep(0.01)
        f = open("fitness" + str(self.myID) + ".txt", "r")
        self.fitness = float(f.read())
        f.close()
        os.system("rm fitness" + str(self.myID) + ".txt")

    def Mutate(self):
        randomRow = random.randint(0, 2)
        randomColumn = random.randint(0, 1)
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
        pyrosim.Send_Cube(name="Torso", pos=[1, 0, 1.5], size=[1, 1, 1])

        # create a joint for BackLeg and Torso
        pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso", child="BackLeg",
                           type="revolute", position=[0.5, 0, 1])

        # create a BackLeg
        pyrosim.Send_Cube(name="BackLeg", pos=[-0.5, 0, -0.5], size=[1, 1, 1])

        # create a second joint for torso and front leg
        pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso", child="FrontLeg",
                           type="revolute", position=[1.5, 0, 1])

        # create front leg
        pyrosim.Send_Cube(name="FrontLeg", pos=[0.5, 0, -0.5], size=[1, 1, 1])

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
        for currentRow in range(3):
            for currentColumn in range(2):
                pyrosim.Send_Synapse(sourceNeuronName=currentRow, targetNeuronName=currentColumn + 3,
                                     weight=self.weights[currentRow][currentColumn])

        # stop pyrosim
        pyrosim.End()
