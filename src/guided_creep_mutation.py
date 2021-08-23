# versión 0.0

import random
from math import floor, ceil
import file_handler


# Comment structure: # $Restriction # $Involved_variables
def fitness(chromosome, n_people, n_tareas):
    constraints = []
    cost = 0
    people = [0] * n_people
    i = 0
    while i < len(chromosome): # HC1 # P
        p = chromosome[i][2]
        people[p - 1] = people[p - 1] + 1 
        i = i + 1
    if max(people) > ceil(n_tareas/n_people): # HC1: distribución equitativa de tareas
        # print(max(people), floor(n_tareas/n_people))
        cost = cost + 100
        constraints.append(1)
    
    return [constraints, cost]


# Comment structure: # $Restriction # $Involved_variables
def guided_creep_mutation(population, fitResult, n_people):
    for chromosome in range(len(population)):
        #print(population[chromosome])
        constraints = fitResult[chromosome][0]
        for chore in population[chromosome]:
            person_changed = False

            # Mutación según restricción violada
            if 1 in constraints: # HC1 #P
                r = random.random()
                if r < 0.5:
                    chore[2] += 1
                    chore[2] %= n_people + 1
                    if chore[2] == 0:
                        chore[2] = 1
                    person_changed = True
    return  


def ga(dimension, varbound, availability, house_chores):
    # week feeder
    
    # Initialize population
    population = []
    for elem in range(10): # 10 chromosomes
        chromosome = []
        for elem in house_chores:
            for e in range(elem[1]):
                chromosome.append([0, 0, 0])
        for elem in chromosome:
            i = 0
            while i < dimension:
                elem[i] = random.randint(varbound[i][0], varbound[i][1])
                i = i + 1
        population.append(chromosome)
    # Fitness evaluation
    n_people = len(availability)
    n_chores = sum(x[1] for x in house_chores)
    # print(n_chores, n_people)
    fitResult = [fitness(p, n_people, n_chores) for p in population]
    # Mutation
    #print(fitResult)
    guided_creep_mutation(population, fitResult, n_people)
    fitResult = [fitness(p, n_people, n_chores) for p in population]
    print(fitResult)
    guided_creep_mutation(population, fitResult, n_people)
    fitResult = [fitness(p, n_people, n_chores) for p in population]
    print(fitResult)
    best = fitResult.index(min(fitResult, key = lambda x: x[1]))
    print_timetable(house_chores, population[best])
    print(population[best])
    # Evaluate fitness 
