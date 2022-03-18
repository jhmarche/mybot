from solution import SOLUTION
import constants as c
import copy
import os


class PARALLEL_HILL_CLIMBER:
    def __init__(self):
        os.system("rm brain*.nndf")
        os.system("rm fitness*.txt")
        self.parents = {}
        self.nextAvailableID = 0
        for x in range(c.populationSize):
            new_solution = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1
            self.parents[x] = new_solution

    def Evolve(self):
        self.Evaluate(self.parents)
        for currentGeneration in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation()

    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.Evaluate(self.children)
        #self.Select()
        #self.Print()

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
        if self.parent.fitness > self.child.fitness:
            self.parent = self.child

    def Print(self):
        print("Parent Fitness: ", self.parent.fitness, "Child Fitness:", self.child.fitness)

    def Show_Best(self):
        pass
        #self.parent.Evaluate("GUI")

    def Evaluate(self, solutions):
        for parent in solutions.values():
            parent.Start_Simulation("GUI")
        for parent in solutions.values():
            parent.Wait_For_Simulation_To_End()

