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

    # create torso for robot
    pyrosim.Send_Cube(name="Torso", pos=[0, 0, 0.5], size=[1, 1, 1])

    # stop pyrosim
    pyrosim.End()


# create the world
create_world()

# create the robot in the world
create_robot()
