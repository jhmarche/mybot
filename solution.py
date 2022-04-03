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
                           type="revolute", position=[0.25, -0.5, 1], jointAxis="1 0 0")

        # create a BackLeg
        pyrosim.Send_Cube(name="BackLeg", pos=[0, -0.5, 0.], size=[0.2, 1, 0.2])

        # create a second joint for torso and front leg
        pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso", child="FrontLeg",
                           type="revolute", position=[0.25, 0.5, 1], jointAxis="1 0 0")

        # create front leg
        pyrosim.Send_Cube(name="FrontLeg", pos=[0, 0.5, 0], size=[0.2, 1, 0.2])

        # create a joint for BackLeg and Torso
        pyrosim.Send_Joint(name="Torso_LeftLeg", parent="Torso", child="LeftLeg",
                           type="revolute", position=[-0.5, 0.25, 1], jointAxis="0 1 0")

        # create a LeftLeg
        pyrosim.Send_Cube(name="LeftLeg", pos=[-0.5, 0, 0], size=[1.0, 0.2, 0.2])

        # create a second joint for torso and right leg
        pyrosim.Send_Joint(name="Torso_RightLeg", parent="Torso", child="RightLeg",
                           type="revolute", position=[0.5, 0.25, 1], jointAxis="0 1 0")

        # create right leg
        pyrosim.Send_Cube(name="RightLeg", pos=[0.5, 0, 0], size=[1.0, 0.2, 0.2])

        # create a second joint for front leg and front lower leg
        pyrosim.Send_Joint(name="FrontLeg_FrontLowerLeg", parent="FrontLeg", child="FrontLowerLeg",
                           type="revolute", position=[0, 1, 0], jointAxis="1 0 0")

        # create front lower leg
        pyrosim.Send_Cube(name="FrontLowerLeg", pos=[0, 0, -0.5], size=[0.2, 0.2, 1.0])

        # create a second joint for back leg and back lower leg
        pyrosim.Send_Joint(name="BackLeg_BackLowerLeg", parent="BackLeg", child="BackLowerLeg",
                           type="revolute", position=[0, -1, 0], jointAxis="1 0 0")

        # create back lower leg
        pyrosim.Send_Cube(name="BackLowerLeg", pos=[0, 0, -0.5], size=[0.2, 0.2, 1.0])

        # create a second joint for left leg and left lower leg
        pyrosim.Send_Joint(name="LeftLeg_LeftLowerLeg", parent="LeftLeg", child="LeftLowerLeg",
                           type="revolute", position=[-1, 0, 0], jointAxis="0 1 0")

        # create left lower leg
        pyrosim.Send_Cube(name="LeftLowerLeg", pos=[0, 0, -0.5], size=[0.2, 0.2, 1.0])

        # create a second joint for right leg and right lower leg
        pyrosim.Send_Joint(name="RightLeg_RightLowerLeg", parent="RightLeg", child="RightLowerLeg",
                           type="revolute", position=[1, 0, 0], jointAxis="0 1 0")

        # create right lower leg
        pyrosim.Send_Cube(name="RightLowerLeg", pos=[0, 0, -0.5], size=[0.2, 0.2, 1.0])

        # create a joint for BackLeg and Torso
        pyrosim.Send_Joint(name="Torso_BackLeg2", parent="Torso", child="BackLeg2",
                           type="revolute", position=[-0.25, -0.5, 1], jointAxis="1 0 0")

        # create a BackLeg
        pyrosim.Send_Cube(name="BackLeg2", pos=[0, -0.5, 0.], size=[0.2, 1, 0.2])

        # create a second joint for torso and front leg
        pyrosim.Send_Joint(name="Torso_FrontLeg2", parent="Torso", child="FrontLeg2",
                           type="revolute", position=[-0.25, 0.5, 1], jointAxis="1 0 0")

        # create front leg
        pyrosim.Send_Cube(name="FrontLeg2", pos=[0, 0.5, 0], size=[0.2, 1, 0.2])

        # create a joint for BackLeg and Left leg2
        pyrosim.Send_Joint(name="Torso_LeftLeg2", parent="Torso", child="LeftLeg2",
                           type="revolute", position=[-0.5, -0.25, 1], jointAxis="0 1 0")

        # create a Left Leg2
        pyrosim.Send_Cube(name="LeftLeg2", pos=[-0.5, 0, 0], size=[1.0, 0.2, 0.2])

        # create a second joint for torso and right leg2
        pyrosim.Send_Joint(name="Torso_RightLeg2", parent="Torso", child="RightLeg2",
                           type="revolute", position=[0.5, -0.25, 1], jointAxis="0 1 0")

        # create right leg2
        pyrosim.Send_Cube(name="RightLeg2", pos=[0.5, 0, 0], size=[1.0, 0.2, 0.2])

        # create a second joint for front leg2 and front lower leg2
        pyrosim.Send_Joint(name="FrontLeg2_FrontLowerLeg2", parent="FrontLeg2", child="FrontLowerLeg2",
                           type="revolute", position=[0, 1, 0], jointAxis="1 0 0")

        # create front lower leg
        pyrosim.Send_Cube(name="FrontLowerLeg2", pos=[0, 0, -0.5], size=[0.2, 0.2, 1.0])

        # create a second joint for back leg and back lower leg
        pyrosim.Send_Joint(name="BackLeg2_BackLowerLeg2", parent="BackLeg2", child="BackLowerLeg2",
                           type="revolute", position=[0, -1, 0], jointAxis="1 0 0")

        # create back lower leg
        pyrosim.Send_Cube(name="BackLowerLeg2", pos=[0, 0, -0.5], size=[0.2, 0.2, 1.0])

        # create a second joint for left leg and left lower leg
        pyrosim.Send_Joint(name="LeftLeg2_LeftLowerLeg2", parent="LeftLeg2", child="LeftLowerLeg2",
                           type="revolute", position=[-1, 0, 0], jointAxis="0 1 0")

        # create left lower leg
        pyrosim.Send_Cube(name="LeftLowerLeg2", pos=[0, 0, -0.5], size=[0.2, 0.2, 1.0])

        # create a second joint for right leg and right lower leg
        pyrosim.Send_Joint(name="RightLeg2_RightLowerLeg2", parent="RightLeg2", child="RightLowerLeg2",
                           type="revolute", position=[1, 0, 0], jointAxis="0 1 0")

        # create right lower leg
        pyrosim.Send_Cube(name="RightLowerLeg2", pos=[0, 0, -0.5], size=[0.2, 0.2, 1.0])

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

        # create a neuron for torso
        pyrosim.Send_Sensor_Neuron(name=3, linkName="LeftLeg")

        # create a neuron for back leg
        pyrosim.Send_Sensor_Neuron(name=4, linkName="RightLeg")

        # create a neuron for back leg
        pyrosim.Send_Sensor_Neuron(name=5, linkName="BackLowerLeg")

        # create a neuron for front leg
        pyrosim.Send_Sensor_Neuron(name=6, linkName="FrontLowerLeg")

        # create a neuron for torso
        pyrosim.Send_Sensor_Neuron(name=7, linkName="LeftLowerLeg")

        # create a neuron for back leg
        pyrosim.Send_Sensor_Neuron(name=8, linkName="RightLowerLeg")

        # create a neuron for back leg2
        pyrosim.Send_Sensor_Neuron(name=9, linkName="BackLeg2")

        # create a neuron for front leg2
        pyrosim.Send_Sensor_Neuron(name=10, linkName="FrontLeg2")

        # create a neuron for Left leg2
        pyrosim.Send_Sensor_Neuron(name=11, linkName="LeftLeg2")

        # create a neuron for right leg2
        pyrosim.Send_Sensor_Neuron(name=12, linkName="RightLeg2")

        # create a neuron for back leg
        pyrosim.Send_Sensor_Neuron(name=13, linkName="BackLowerLeg2")

        # create a neuron for front leg
        pyrosim.Send_Sensor_Neuron(name=14, linkName="FrontLowerLeg2")

        # create a neuron for torso
        pyrosim.Send_Sensor_Neuron(name=15, linkName="LeftLowerLeg2")

        # create a neuron for torso
        pyrosim.Send_Sensor_Neuron(name=16, linkName="RightLowerLeg2")

        # create neuron for torso/back leg motor
        pyrosim.Send_Motor_Neuron(name=17, jointName="Torso_BackLeg")

        # create neuron for torso/front leg motor
        pyrosim.Send_Motor_Neuron(name=18, jointName="Torso_FrontLeg")

        # create neuron for torso/back leg motor
        pyrosim.Send_Motor_Neuron(name=19, jointName="Torso_LeftLeg")

        # create neuron for torso/front leg motor
        pyrosim.Send_Motor_Neuron(name=20, jointName="Torso_RightLeg")

        # create neuron for torso/back leg motor
        pyrosim.Send_Motor_Neuron(name=21, jointName="BackLeg_BackLowerLeg")

        # create neuron for torso/front leg motor
        pyrosim.Send_Motor_Neuron(name=22, jointName="FrontLeg_FrontLowerLeg")

        # create neuron for torso/back leg motor
        pyrosim.Send_Motor_Neuron(name=23, jointName="LeftLeg_LeftLowerLeg")

        # create neuron for torso/front leg motor
        pyrosim.Send_Motor_Neuron(name=24, jointName="RightLeg_RightLowerLeg")

        # create neuron for torso/back leg2 motor
        pyrosim.Send_Motor_Neuron(name=25, jointName="Torso_BackLeg2")

        # create neuron for torso/front leg2 motor
        pyrosim.Send_Motor_Neuron(name=26, jointName="Torso_FrontLeg2")

        # create neuron for torso/left leg2 motor
        pyrosim.Send_Motor_Neuron(name=27, jointName="Torso_LeftLeg2")

        # create neuron for torso/right leg2 motor
        pyrosim.Send_Motor_Neuron(name=28, jointName="Torso_RightLeg2")

        # create neuron for torso/back leg motor
        pyrosim.Send_Motor_Neuron(name=29, jointName="BackLeg2_BackLowerLeg2")

        # create neuron for torso/front leg motor
        pyrosim.Send_Motor_Neuron(name=30, jointName="FrontLeg2_FrontLowerLeg2")

        # create neuron for torso/back leg motor
        pyrosim.Send_Motor_Neuron(name=31, jointName="LeftLeg2_LeftLowerLeg2")

        # create neuron for torso/front leg motor
        pyrosim.Send_Motor_Neuron(name=32, jointName="RightLeg2_RightLowerLeg2")

        # nested for loops that creates a synapse from each neuron to each motor
        for currentRow in range(c.numSensorNeurons):
            for currentColumn in range(c.numMotorNeurons):
                pyrosim.Send_Synapse(sourceNeuronName=currentRow, targetNeuronName=currentColumn + c.numSensorNeurons,
                                     weight=self.weights[currentRow][currentColumn])

        # stop pyrosim
        pyrosim.End()