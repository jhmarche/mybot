import pyrosim.pyrosim as pyrosim

# file to store information about world
pyrosim.Start_SDF("boxes.sdf")

#set size of cube
length = 1
width = 1
height = 1

#set position of cube
x = 0
y = 0
z = 0.5

# parameters for the box
pyrosim.Send_Cube(name="Box", pos=[x, y, z], size=[length, width, height])
pyrosim.Send_Cube(name="Box2", pos=[x, y, z], size=[length, width, height])

# stop pyrosim
pyrosim.End()