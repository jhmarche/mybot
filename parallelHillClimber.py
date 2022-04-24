from solution import SOLUTION
import constants as c
import copy
import os
import numpy

class PARALLEL_HILL_CLIMBER:
    def __init__(self):
        os.system("rm brain*.nndf")
        os.system("rm fitness*.txt")
        self.parents = {}
        self.nextAvailableID = 0
        self.matrix = numpy.zeros((c.populationSize, c.numberOfGenerations))
        for x in range(c.populationSize):
            new_solution = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1
            self.parents[x] = new_solution

    def Evolve(self):
        self.Evaluate(self.parents)
        for currentGeneration in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation()
            for i in range(c.populationSize):
                self.matrix[i][currentGeneration] = self.parents[i].fitness

    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.Evaluate(self.children)
        self.Select()
        self.Print()

    def Spawn(self):
        self.children = {}
        for key in self.parents.keys():
            self.children[key] = copy.deepcopy(self.parents[key])
            self.children[key].Set_ID(self.nextAvailableID)
            self.nextAvailableID += 1

    def Mutate(self):
        for child in self.children.values():
            child.Mutate()

    def Select(self):
        for i in range(c.populationSize):
            if self.parents[i].fitness > self.children[i].fitness:
                self.parents[i] = self.children[i]

    def Print(self):
        for i in range(c.populationSize):
            print("\nParent Fitness: ", self.parents[i].fitness, "Child Fitness:", self.children[i].fitness, "\n")

    def Show_Best(self):
        best_fitness = 0
        for i in range(c.populationSize):
            if self.parents[i].fitness < self.parents[best_fitness].fitness:
                best_fitness = i
        self.parents[best_fitness].Start_Simulation("GUI")

    def Evaluate(self, solutions):
        for parent in solutions.values():
            parent.Start_Simulation("DIRECT")
        for parent in solutions.values():
            parent.Wait_For_Simulation_To_End()
        numpy.savetxt("Test.txt", self.matrix)
        numpy.save("octoped.npy", self.matrix)

