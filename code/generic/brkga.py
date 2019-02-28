
import math
import numpy as np
import data as data
from interfaces.algorithmInterface import Algorithm


class BRKGA(Algorithm):

    # functions:
    # self.decode(individual['chr'])
    # self.generate_chromosome()

    def initializePopulation(self, numIndividuals, input):
        population = []

        for i in range(numIndividuals):
            # chromosome = list(np.random.randint(
                # low=0, high=self.config["max_chr_value"], size=chrLength))
            chromosome = self.generate_chromosome(input)
            population.append(
                {'chr': chromosome, 'solution': {}, 'fitness': None})
        
        return(population)

    def classifyIndividuals(self, population, numElite):
        fitness = np.array([e['fitness'] for e in population])
        order = sorted(range(len(fitness)), key=lambda k: fitness[k])
        whichElite = order[0:numElite]
        whichNonElite = order[numElite:(len(fitness))]
        population = np.array(population)
        elite = population[whichElite]
        nonElite = population[whichNonElite]
        return list(elite), list(nonElite)

    def generateMutantIndividuals(self, numMutants, input):
        mutants = []

        for i in range(numMutants):
            chromosome = self.generate_chromosome(input)
            mutants.append(
                {'chr': chromosome, 'solution': {}, 'fitness': None})

        return mutants

    def doCrossover(self, elite, nonelite, ro, numCrossover):
        crossover = []
        for i in range(numCrossover):
            indexElite = int(math.floor(np.random.rand()*len(elite)))
            indexNonElite = int(math.floor(np.random.rand()*len(nonelite)))
            chrElite = elite[indexElite]['chr']
            chrNonElite = nonelite[indexNonElite]['chr']
            rnd = list(np.random.rand(len(chrElite)))
            chrCross = [chrElite[i] if rnd[i] <= ro else chrNonElite[i]
                        for i in range(len(chrElite))]
            crossover.append(
                {'chr': chrCross, 'solution': {}, 'fitness': None})
        return crossover

    def getBestFitness(self, population):
        fitness = np.array([e['fitness'] for e in population])
        order = sorted(range(len(fitness)), key=lambda k: fitness[k])
        return population[order[0]]

    def decodeAll(self, population, input):
        for individual in population:
            individual['solution'] = self.decode(individual['chr'], input)
            individual['fitness'] = individual['solution'].value()

    def solve(self, input, current=Solution()):

        # initializations
        numIndividuals = self.config["num_individuals"]
        numElite = math.ceil(numIndividuals*self.config["per_elite"])
        numMutants = math.ceil(numIndividuals*self.config["per_mutants"])
        numCrossover = max(numIndividuals-numElite-numMutants, 0)

        maxNumGen = self.config["max_num_gen"])
        ro=self.config["inheritance_prob"])

        evol=[]

        # Main body
        population=self.initializePopulation(numIndividuals, input)

        i=0
        while (i < maxNumGen):
            population=self.decodeAll(population, input)
            bestFitness=self.getBestFitness(population)
            evol.append(bestFitness['fitness'])
            print bestFitness

            if numElite > 0:
                elite, nonelite=self.classifyIndividuals(
                    population, numElite)
            else:
                elite=[]
                nonelite=population

            if numMutants > 0:
                mutants=self.generateMutantIndividuals(
                    numMutants, input)
            else:
                mutants=[]

            if numCrossover > 0:
                crossover=self.doCrossover(
                    elite, nonelite, ro, numCrossover)
            else:
                crossover=[]

            population=elite + crossover + mutants
            i += 1

        population=self.decodeAll(population, input)
        bestIndividual=self.getBestFitness(population)

        return solution
