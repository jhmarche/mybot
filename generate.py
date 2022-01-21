import pyrosim.pyrosim as pyrosim

# file to store information about world
pyrosim.Start_SDF("boxes.sdf")

#set size of cube
length = 1
width = 1
height = 1

# set position of cube
x = 0
y = 0
z = 0.5

# creates a tower of boxes that get smaller as they get higher
for i in range(6):
    for j in range(6):
        length = 1
        width = 1
        height = 1
        for k in range(10):
            pyrosim.Send_Cube(name="Box", pos=[i, j, k], size=[length, width, height])
            #z += height
            length *= 0.9
            width *= 0.9
            height *= 0.9

# stop pyrosim
pyrosim.End()