import numpy
import matplotlib.pyplot

backLegSensorValues = numpy.load("../mybot/data/backLegSensorValues.npy")
frontLegSensorValues = numpy.load("../mybot/data/backLegSensorValues.npy")
targetAngles = numpy.load("../mybot/data/targetAngles.npy")

#matplotlib.pyplot.plot(backLegSensorValues, label="BackLeg", linewidth=10)
#matplotlib.pyplot.plot(frontLegSensorValues, label="FrontLeg")
matplotlib.pyplot.plot(targetAngles, numpy.sin(targetAngles), label="TargetAngles")
matplotlib.pyplot.legend()
matplotlib.pyplot.show()