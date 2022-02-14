import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy
import random

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.setGravity(0, 0, -9.8)
# reads in world described in box.sdf
p.loadSDF("world.sdf")
planeId = p.loadURDF("plane.urdf")

robotId = p.loadURDF("body.urdf")

# used to simulate sensors
pyrosim.Prepare_To_Simulate(robotId)

# variables for robot
backLegAmplitude = numpy.pi / 4
backLegFrequency = 10
backLegPhaseOffset = numpy.pi/4
frontLegAmplitude = numpy.pi / 4
frontLegFrequency = 10
frontLegPhaseOffset = 0

# vector for backleg sensor values
backLegSensorValues = numpy.zeros(1000)

# vector for frontleg sensor values
frontLegSensorValues = numpy.zeros(1000)

# vector for target angles of back leg to be used by robot
backLegTargetAngles = numpy.linspace(0, 2 * numpy.pi, 1000)
for x in range(len(backLegTargetAngles)):
    backLegTargetAngles[x] = backLegAmplitude * numpy.sin(backLegFrequency *
                                                          backLegTargetAngles[x] + backLegPhaseOffset)
# numpy.save("../mybot/data/backLegTargetAngles.npy", backLegTargetAngles)

# vector fot target angles of front leg to be used by robot
frontLegTargetAngles = numpy.linspace(0, 2 * numpy.pi, 1000)
for x in range(len(frontLegTargetAngles)):
    frontLegTargetAngles[x] = frontLegAmplitude * numpy.sin(frontLegFrequency *
                                                            frontLegTargetAngles[x] + frontLegPhaseOffset)
# numpy.save("../mybot/data/frontLegTargetAngles.npy", frontLegTargetAngles)
# exit()

# for loop to make simulation last longer
for i in range(1000):
    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    pyrosim.Set_Motor_For_Joint(
        bodyIndex=robotId,
        jointName="Torso_BackLeg",
        controlMode=p.POSITION_CONTROL,
        targetPosition=backLegTargetAngles[i],
        maxForce=25
    )
    pyrosim.Set_Motor_For_Joint(
        bodyIndex=robotId,
        jointName="Torso_FrontLeg",
        controlMode=p.POSITION_CONTROL,
        targetPosition=frontLegTargetAngles[i],
        maxForce=25
    )
    time.sleep(1 / 60)

p.disconnect()

print(backLegSensorValues)
print(frontLegSensorValues)
numpy.save("../mybot/data/backLegSensorValues.npy", backLegSensorValues)
numpy.save("../mybot/data/frontLegSensorValues.npy", frontLegSensorValues)
