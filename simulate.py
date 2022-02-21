from simulation import SIMULATION
# import pybullet as p
# import time
# import pybullet_data
# import pyrosim.pyrosim as pyrosim
# import numpy
# import constants as c
# import random
#

# # variables for robot
# backLegAmplitude = c.PI_OVER_FOUR
# backLegFrequency = c.FIVE
# backLegPhaseOffset = c.ZERO
# frontLegAmplitude = c.PI_OVER_FOUR
# frontLegFrequency = c.FIVE
# frontLegPhaseOffset = c.ZERO
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

#
# print(backLegSensorValues)
# print(frontLegSensorValues)
# numpy.save("../mybot/data/backLegSensorValues.npy", backLegSensorValues)
# numpy.save("../mybot/data/frontLegSensorValues.npy", frontLegSensorValues)
simulation = SIMULATION()
simulation.Run()
