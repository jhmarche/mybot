import numpy
import matplotlib.pyplot

quadrupedMatrix = numpy.load("../mybot/quadruped.npy")
octopedMatrix = numpy.load("../mybot/octoped.npy")


matplotlib.pyplot.plot(quadrupedMatrix[0, :], label="Quadruped")
matplotlib.pyplot.plot(octopedMatrix[0, :], label="Octoped")

#count = 0
#for row in quadrupedMatrix:
#    count +=1
#    matplotlib.pyplot.plot(row, label="Quadruped " + " " + str(count))
#count = 0
#for row in octopedMatrix:
#    count+=1
#    matplotlib.pyplot.plot(row, label="Octoped " + " " + str(count))
matplotlib.pyplot.legend()
matplotlib.pyplot.show()

