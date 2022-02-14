import numpy
import matplotlib.pyplot

backLegSensorValues = numpy.load("../mybot/data/backLegSensorValues.npy")
frontLegSensorValues = numpy.load("../mybot/data/backLegSensorValues.npy")
backLegTargetAngles = numpy.load("../mybot/data/backLegTargetAngles.npy")
frontLegTargetAngles = numpy.load("../mybot/data/frontLegTargetAngles.npy")

#matplotlib.pyplot.plot(backLegSensorValues, label="BackLeg", linewidth=10)
#matplotlib.pyplot.plot(frontLegSensorValues, label="FrontLeg")
matplotlib.pyplot.plot(backLegTargetAngles, label="BackLeg")
matplotlib.pyplot.plot(frontLegTargetAngles, label="FrontLeg")
matplotlib.pyplot.xlabel('Angle [rad]')
matplotlib.pyplot.ylabel('sin(x)')
matplotlib.pyplot.axis('tight')
matplotlib.pyplot.legend()
matplotlib.pyplot.show()