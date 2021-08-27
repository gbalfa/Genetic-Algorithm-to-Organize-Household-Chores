import guided_creep_mutation as gcm
import data_generation
from file_handler import arrangeSchedules, readCSV

n_week_days = 6
n_time_slots = 6
n_people = 2

# Data generation
max_frecuency = 1
max_priority = 3
n_chores = 10
data_generation.generateScheduleData("data/schedules.csv", n_people, n_week_days, n_time_slots)
data_generation.generateChoreData("data/chores.csv", n_chores, max_frecuency, max_priority)

# Representation of availability in time slots P X D X T 
schedules = arrangeSchedules(readCSV("data/schedules.csv"), n_week_days)

# Chores (recurrence/week):  [chore, frecuency, priority]
chores = readCSV("data/chores.csv")

# WSP
varbound = [[0, n_week_days - 1], [0, n_time_slots - 1], [0, n_people - 1]]

# # model run
gcm.ga(dimension=3, varbound=varbound, schedules=schedules, chores=chores)
