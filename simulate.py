import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim

# physics client for pybullet
physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.setGravity(0, 0, -9.8)
# reads in world described in box.sdf
p.loadSDF("world.sdf")
planeId = p.loadURDF("plane.urdf")

robotId = p.loadURDF("body.urdf")

# used to simulate sensors
pyrosim.Prepare_To_Simulate(robotId)

# for loop to make simulation last longer
for x in range(1000):
    p.stepSimulation()
    backLegTouch = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    time.sleep(1/60)
    print(x)

p.disconnect()