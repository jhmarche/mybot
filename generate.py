import pyrosim.pyrosim as pyrosim


# function to create the world
def create_world():
    # file to store information about world
    pyrosim.Start_SDF("world.sdf")

    # creates a box
    pyrosim.Send_Cube(name="Box", pos=[0, 0, 0.5], size=[1, 1, 1])

    # stop pyrosim
    pyrosim.End()


# create the world
create_world()
