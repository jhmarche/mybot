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

    # create link0
    pyrosim.Send_Cube(name="Link0", pos=[0, 0, 0.5], size=[1, 1, 1])

    # create a joint for link0 and link1
    pyrosim.Send_Joint(name="Link0_Link1", parent="Link0", child="Link1",
                       type="revolute", position=[0, 0, 1.0])

    # create link1
    pyrosim.Send_Cube(name="Link1", pos=[0, 0, 0.5], size=[1, 1, 1])

    # create a second joint for link1 and link2
    pyrosim.Send_Joint(name="Link1_Link2", parent="Link1", child="Link2",
                       type="revolute", position=[0, 0, 1])

    # create link2
    pyrosim.Send_Cube(name="Link2", pos=[0, 0, 0.5], size=[1, 1, 1])

    # create a third joint for link2 and link3
    pyrosim.Send_Joint(name="Link2_Link3", parent="Link2", child="Link3",
                       type="revolute", position=[0, 0.5, 0.5])

    # create link3
    pyrosim.Send_Cube(name="Link3", pos=[0, 0.5, 0], size=[1, 1, 1])

    # create a fourth joint for link3 and link4
    pyrosim.Send_Joint(name="Link3_Link4", parent="Link3", child="Link4",
                       type="revolute", position=[0, 1, 0])

    # create link4
    pyrosim.Send_Cube(name="Link4", pos=[0, 0.5, 0], size=[1, 1, 1])

    # create a fifth joint for link4 and link5
    pyrosim.Send_Joint(name="Link4_Link5", parent="Link4", child="Link5",
                       type="revolute", position=[0, 0.5, -0.5])

    # create link5
    pyrosim.Send_Cube(name="Link5", pos=[0, 0, -0.5], size=[1, 1, 1])

    # create a sixth joint for link5 and link6
    pyrosim.Send_Joint(name="Link5_Link6", parent="Link5", child="Link6",
                       type="revolute", position=[0, 0, -1])

    # create link5
    pyrosim.Send_Cube(name="Link6", pos=[0, 0, -0.5], size=[1, 1, 1])


    # stop pyrosim
    pyrosim.End()


# create the world
create_world()

# create the robot in the world
create_robot()
