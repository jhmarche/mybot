import pyrosim.pyrosim as pyrosim

# file to store information about world
pyrosim.Start_SDF("box.sdf")

#set size of cube
length = 1
width = 1
height = 1

# parameters for the box
pyrosim.Send_Cube(name="Box", pos=[0, 0, 0.5], size=[length, width, height])

# stop pyrosim
pyrosim.End()