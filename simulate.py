from simulation import SIMULATION
import sys

directOrGUI = sys.argv[1]

# Run the simulation of a robot
simulation = SIMULATION(directOrGUI)
simulation.Run()
simulation.Get_Fitness()

