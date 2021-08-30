'''
Genetic algorithm for scheduling problem
'''

import numpy as np
from myga import geneticalgorithm as ga
import data_generation
from file_handler import arrangeSchedules, readCSV
from data_visualization import heatMapsFromCromosome
from math import ceil, floor, log2
import copy

n_week_days = 6
n_time_slots_day = 6
n_people = 2

n_chores = 25
max_frecuency = 1
max_priority = 3

n_time_slots = n_week_days * n_time_slots_day

# Data generation
data_generation.generateScheduleData("data/schedules.csv", n_people,
                                     n_week_days, n_time_slots_day)
data_generation.generateChoreData("data/chores.csv", n_chores, max_frecuency,
                                  max_priority)

# Representation of availability in time slots
schedule_fields, schedules = arrangeSchedules(
    readCSV("data/schedules.csv"), n_week_days)

# Chores (recurrence/week):  [chore, frecuency, priority]
chores = readCSV("data/chores.csv")

# dimension: (timeslot + person) * events
size_event_chunk = 2
dimension = size_event_chunk * n_chores


def myFitness(X):
    # HC0: tope horario
    # HC1: distribución carga de eventos por persona
    # SFT0: prioridad eventos
    # SFT1
    # SFT2
    local_schedules = copy.deepcopy(schedules)  # to represent used schedules
    costs_hcs = [100, 50]  # Hard constraints costs
    costs_scs = [10, 5, 1]  # Soft constraints costs
    events_per_person = [0] * n_people
    cost = 0
    i = 0
    event = 0
    while i < len(X):
        # decode
        dec_tSlot = np.int_(X[i])
        dec_person = np.int_(X[i + 1])

        if local_schedules[dec_person][dec_tSlot] == 0:  # HC0
            cost += costs_hcs[0]
        else:
            local_schedules[dec_person][dec_tSlot] = 0
            events_per_person[dec_person] += 1  # HC1

        event = event + 1
        i = i + size_event_chunk

    if max(events_per_person) > ceil(1 * (n_chores / n_people)):  # HC1
        cost += costs_hcs[1]

    return cost


algorithm_param = {
    'max_num_iteration': 1000,
    'population_size': 100,
    'mutation_probability': 0.1,
    'elit_ratio': 0.01,
    'crossover_probability': 0.5,
    'parents_portion': 0.3,
    'crossover_type': 'uniform',
    'max_iteration_without_improv': None
}

varbound = np.array([[0, n_time_slots - 1], [0, n_people - 1]] * n_chores)
vartype = np.array([['int'], ['int']] * n_chores)

# model
model = ga(function=myFitness,
           dimension=2 * n_chores,
           variable_type_mixed=vartype,
           variable_boundaries=varbound,
           algorithm_parameters=algorithm_param)

model.run()
output = model.output_dict
rows = heatMapsFromCromosome(
    output['variable'], n_week_days, n_time_slots_day, size_event_chunk, schedule_fields, schedules)
# print(rows)
# print(output['variable'])
# print(output['function'])
