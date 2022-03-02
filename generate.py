import pyrosim.pyrosim as pyrosim


# function to create world
def Generate_World():
    # file to store information about world
    pyrosim.Start_SDF("world.sdf")

    # creates a box
    pyrosim.Send_Cube(name="Box", pos=[-3, 3, 0.5], size=[1, 1, 1])

    # stop pyrosim
    pyrosim.End()


# function to create body of robot
def Generate_Body():
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
def Generate_Brain():
    # file to store brain of robot
    pyrosim.Start_NeuralNetwork("brain.nndf")

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

    # create a synapse from neuron 0 to neuron 3
    pyrosim.Send_Synapse(sourceNeuronName=0, targetNeuronName=3, weight=1.0)

    # stop pyrosim
    pyrosim.End()


Generate_World()

Generate_Body()

Generate_Brain()
