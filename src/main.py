'''
Using ga with only bool variables
variable_type = 'bool'
'''

import numpy as np
from myga import geneticalgorithm as ga
import data_generation
from file_handler import arrangeSchedules, readCSV
from data_visualization import heatMapsFromCromosome
from math import ceil, floor, log2
import copy

n_week_days = 1
n_time_slots_day = 2
n_people = 2

n_chores = 2
max_frecuency = 1
max_priority = 3

n_time_slots = n_week_days * n_time_slots_day

# Data generation
data_generation.generateScheduleData("data/schedules.csv", n_people,
                                     n_week_days, n_time_slots_day)
data_generation.generateChoreData("data/chores.csv", n_chores, max_frecuency,
                                  max_priority)

# Representation of availability in time slots
schedules = arrangeSchedules(readCSV("data/schedules.csv"), n_week_days)

# Chores (recurrence/week):  [chore, frecuency, priority]
chores = readCSV("data/chores.csv")

# WSP: 0 to value for indexing purpouse
varbound = [[0, n_week_days - 1], [0, n_time_slots - 1], [0, n_people - 1]]

# enc: encoded
# dimension: (timeslot + person) * events
size_enc_tSlot = ceil(log2(n_time_slots))
size_enc_person = ceil(log2(n_people))
size_event_chunk = size_enc_tSlot + size_enc_person
dimension = size_event_chunk * n_chores


def myFitness(X):
    # HC0: tope horario
    # HC1: distribución carga de eventos por persona
    # SFT0 : prioridad eventos
    # SFT1
    # SFT2
    local_schedules = copy.deepcopy(schedules)  # to represent used schedules
    costs_hcs = [100, 50]  # Hard constraints costs
    costs_scs = [10, 5, 1]  # Soft constraints costs
    events_per_person = [0] * n_people
    cost = 0
    i = 0
    event = 0
    while i < dimension:
        enc_tSlot = X[i:(i + size_enc_tSlot)]
        enc_person = X[(i + size_enc_tSlot):(i + size_enc_tSlot +
                                             size_enc_person)]

        # decode
        dec_tSlot = np.int_(enc_tSlot.dot(2**np.arange(size_enc_tSlot)[::-1]))
        dec_person = np.int_(
            enc_person.dot(2**np.arange(size_enc_person)[::-1]))

        # invalid configurations
        if dec_tSlot >= n_time_slots or dec_person >= n_people:
            return 10000

        if local_schedules[dec_person][dec_tSlot] == 0:  # HC0
            cost += costs_hcs[0]
        else:
            local_schedules[dec_person][dec_tSlot] = 0
            events_per_person[dec_person] += 1  # HC1

        event = event + 1
        i = i + size_event_chunk

    if max(events_per_person) > ceil(1.5 * (n_chores / n_people)):  # HC1
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

# model
model = ga(function=myFitness,
           dimension=dimension,
           variable_type='bool',
           algorithm_parameters=algorithm_param)

model.run()
# output = model.output_dict
# print(output['variable'])
# print(output['function'])
