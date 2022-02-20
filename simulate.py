from simulation import SIMULATION
# import pybullet as p
# import time
# import pybullet_data
# import pyrosim.pyrosim as pyrosim
# import numpy
# import constants as c
# import random
#
# physicsClient = p.connect(p.GUI)
# p.setAdditionalSearchPath(pybullet_data.getDataPath())
#
# p.setGravity(c.ZERO, c.ZERO, -9.8)
# # reads in world described in box.sdf
# p.loadSDF("world.sdf")
# planeId = p.loadURDF("plane.urdf")
#
# robotId = p.loadURDF("body.urdf")
#
# # used to simulate sensors
# pyrosim.Prepare_To_Simulate(robotId)
#
# # variables for robot
# backLegAmplitude = c.PI_OVER_FOUR
# backLegFrequency = c.FIVE
# backLegPhaseOffset = c.ZERO
# frontLegAmplitude = c.PI_OVER_FOUR
# frontLegFrequency = c.FIVE
# frontLegPhaseOffset = c.ZERO
#
# # vector for backleg sensor values
# backLegSensorValues = numpy.zeros(c.ITERATIONS)
#
# # vector for frontleg sensor values
# frontLegSensorValues = numpy.zeros(c.ITERATIONS)
#
# # vector for target angles of back leg to be used by robot
# backLegTargetAngles = numpy.linspace(c.ZERO, c.TWO_PI, c.ITERATIONS)
# for x in range(len(backLegTargetAngles)):
#     backLegTargetAngles[x] = backLegAmplitude * numpy.sin(backLegFrequency *
#                                                           backLegTargetAngles[x] + backLegPhaseOffset)
# # numpy.save("../mybot/data/backLegTargetAngles.npy", backLegTargetAngles)
#
# # vector fot target angles of front leg to be used by robot
# frontLegTargetAngles = numpy.linspace(c.ZERO, c.TWO_PI, c.ITERATIONS)
# for x in range(len(frontLegTargetAngles)):
#     frontLegTargetAngles[x] = frontLegAmplitude * numpy.sin(frontLegFrequency *
#                                                             frontLegTargetAngles[x] + frontLegPhaseOffset)
# # numpy.save("../mybot/data/frontLegTargetAngles.npy", frontLegTargetAngles)
# # exit()
#
# # for loop to make simulation last longer
# for i in range(c.ITERATIONS):
#     p.stepSimulation()
#     backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
#     frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
#     pyrosim.Set_Motor_For_Joint(
#         bodyIndex=robotId,
#         jointName="Torso_BackLeg",
#         controlMode=p.POSITION_CONTROL,
#         targetPosition=backLegTargetAngles[i],
#         maxForce=c.TEN
#     )
#     pyrosim.Set_Motor_For_Joint(
#         bodyIndex=robotId,
#         jointName="Torso_FrontLeg",
#         controlMode=p.POSITION_CONTROL,
#         targetPosition=frontLegTargetAngles[i],
#         maxForce=c.TEN
#     )
#     time.sleep(c.SLEEP)
#
# p.disconnect()
#
# print(backLegSensorValues)
# print(frontLegSensorValues)
# numpy.save("../mybot/data/backLegSensorValues.npy", backLegSensorValues)
# numpy.save("../mybot/data/frontLegSensorValues.npy", frontLegSensorValues)
simulation = SIMULATION()
