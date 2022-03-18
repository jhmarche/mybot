from solution import SOLUTION
import constants as c
import copy


class PARALLEL_HILL_CLIMBER:
    def __init__(self):
        self.parents = {}
        self.nextAvailableID = 0
        for x in range(c.populationSize):
            new_solution = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1
            self.parents[x] = new_solution

    def Evolve(self):
        for parent in self.parents.values():
            parent.Evaluate("GUI")
            #for currentGeneration in range(c.numberOfGenerations):
                #self.Evolve_For_One_Generation()

    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.child.Evaluate("DIRECT")
        self.Select()
        self.Print()

    def Spawn(self):
        self.child = copy.deepcopy(self.parent)
        self.child.Set_ID(self.nextAvailableID)
        self.nextAvailableID += 1

    def Mutate(self):
        self.child.Mutate()

    def Select(self):
        if self.parent.fitness > self.child.fitness:
            self.parent = self.child

    def Print(self):
        print("Parent Fitness: ", self.parent.fitness, "Child Fitness:", self.child.fitness)

    def Show_Best(self):
        pass
        #self.parent.Evaluate("GUI")