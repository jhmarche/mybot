import pyrosim.pyrosim as pyrosim

# file to store information about world
pyrosim.Start_SDF("box.sdf")

#set size of cube
length = 1
width = 2
height = 3

#set position of cube
x = 0
y = 0
z = 1.5

# parameters for the box
pyrosim.Send_Cube(name="Box", pos=[x, y, z], size=[length, width, height])

# stop pyrosim
pyrosim.End()