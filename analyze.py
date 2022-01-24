import numpy
import matplotlib.pyplot

backLegSensorValues = numpy.load("../mybot/data/backLegSensorValues.npy")
frontLegSensorValues = numpy.load("../mybot/data/backLegSensorValues.npy")

matplotlib.pyplot.plot(backLegSensorValues, label="BackLeg", linewidth=10)
matplotlib.pyplot.plot(frontLegSensorValues, label="FrontLeg")
matplotlib.pyplot.legend()
matplotlib.pyplot.show()