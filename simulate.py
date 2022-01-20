import pybullet as p
import time
import pybullet_data

# physics client for pybullet
physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.setGravity(0, 0, -9.8)
# reads in world described in box.sdf
p.loadSDF("box.sdf")
planeId = p.loadURDF("plane.urdf")

# for loop to make simulation last longer
for x in range(1000):
    p.stepSimulation()
    time.sleep(1/60)
    print(x)

p.disconnect()