import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy

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

# vector for backleg sensor values
backLegSensorValues = numpy.zeros(1000)

# vector for frontleg sensor values
frontLegSensorValues = numpy.zeros(1000)

# for loop to make simulation last longer
for x in range(1000):
    p.stepSimulation()
    backLegSensorValues[x] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[x] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    time.sleep(1 / 60)

p.disconnect()

print(backLegSensorValues)
print(frontLegSensorValues)
numpy.save("../mybot/data/backLegSensorValues.npy", backLegSensorValues)
numpy.save("../mybot/data/frontLegSensorValues.npy", frontLegSensorValues)