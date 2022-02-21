from simulation import SIMULATION

# # vector for target angles of back leg to be used by robot
# # numpy.save("../mybot/data/backLegTargetAngles.npy", backLegTargetAngles)

# # numpy.save("../mybot/data/frontLegTargetAngles.npy", frontLegTargetAngles)
# # exit()
#
# numpy.save("../mybot/data/backLegSensorValues.npy", backLegSensorValues)
# numpy.save("../mybot/data/frontLegSensorValues.npy", frontLegSensorValues)
simulation = SIMULATION()
simulation.Run()
