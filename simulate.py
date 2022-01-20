import pybullet as p
import time

# physics client for pybullet
physicsClient = p.connect(p.GUI)

p.setGravity(0, 0, -9.8)
# reads in world described in box.sdf
p.loadSDF("box.sdf")

# for loop to make simulation last longer
for x in range(1000):
    p.stepSimulation()
    time.sleep(1/60)
    print(x)

p.disconnect()