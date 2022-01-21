import pyrosim.pyrosim as pyrosim


# function to create the world
def create_world():
    # file to store information about world
    pyrosim.Start_SDF("world.sdf")

    # creates a box
    pyrosim.Send_Cube(name="Box", pos=[-3, 3, 0.5], size=[1, 1, 1])

    # stop pyrosim
    pyrosim.End()


# function to create a robot
def create_robot():
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


# create the world
create_world()

# create the robot in the world
create_robot()
