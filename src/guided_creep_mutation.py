# versión 0.0

import random
from math import floor, ceil
import file_handler
import data_visualization
from collections import Counter
import operator


def busySchedule(schedules, chromosome):
    cost = 0
    for c in range(len(chromosome)):
        weekday = chromosome[c][0]
        slot = chromosome[c][1]
        person = chromosome[c][2]
        print(person, weekday, slot)
        try:
            print(schedules[person])
        except: 
            print("error")
            print(schedules)
        if schedules[person][weekday][slot] == 0:
            cost = cost + 10
    return cost
                # print("tope horario: ", weekday, slot)

# Comment structure: # $Restriction # $Involved_variables
def fitness(chromosome, chores, schedules):
    n_people = len(schedules)
    n_chores = sum(x[1] for x in chores)
    chromosome_len = len(chromosome)

    constraints = []
    cost = 0
    people = [0] * n_people
    i = 0
    # HC1: distribución equitativa de chores
    while i < chromosome_len: # HC1 # P
        p = chromosome[i][2]
        people[p - 1] = people[p - 1] + 1 
        i = i + 1
    if max(people) > ceil(n_chores/n_people): 
        # print(max(people), floor(n_chores/n_people))
        cost = cost + 100
        constraints.append(1)
    # HC2: tope de horarios
    for gen in chromosome:
        cost = cost + busySchedule(schedules, chromosome)    
    
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
    return population


def ga(dimension, varbound, schedules, chores):
    # Initialize population
    population = []
    i = 0
    while i < 10: # 10 chromosomes
        chromosome = []
        for elem in chores:
            for e in range(elem[1]): # frecuency
                chromosome.append([0, 0, 0])
        for elem in chromosome:
            j = 0
            while j < dimension:
                elem[j] = random.randint(varbound[j][0], varbound[j][1])
                j = j + 1
        population.append(chromosome)
        i = i + 1
    
    # Fitness evaluation
    n_people = len(schedules)
    fitResult = [fitness(p, chores, schedules) for p in population]
    best_fitResult = fitResult
    i = 0
    best_min_value = 0
    min_index, min_value = min(enumerate(fitResult), key=lambda x: x[1])
    if min_value[1] == 0:
        return 
    while i < 1000:
        if min_value[1] == 0:
            print("generación: ", i)
            return 
        # Mutation
        population = guided_creep_mutation(population, fitResult, n_people)
        fitResult = [fitness(p, chores, schedules) for p in population]
        min_index, min_value = min(enumerate(fitResult), key=lambda x: x[1])
        print(min_value[1], best_min_value)
        if min_value[1] >= best_min_value:
            i = i + 1
        else:
            best_min_index = min_index
            best_min_value = min_value[1]
            best_fitResult = fitResult
    # print(population[min_index])
    # print(len(population[min_index]))
    # print(best_min_value)
    # print(Counter([str(x[2]) for x in best])) 
    # print(best_fitResult)
    # data_visualization.print_timetable(chores, population[best])
    # print(population[min_index])
    # Evaluate fitness 
