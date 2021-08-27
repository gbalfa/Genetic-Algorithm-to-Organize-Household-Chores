"""
Data generation
"""
import random


def generateScheduleData(filename, n_people, n_week_days, n_time_slots):
    csvfile =  open(filename, 'w')
    csvfile.write('slot0')
    for slot in range(1, n_time_slots): # field names
        csvfile.write(',' + str(slot))
    csvfile.write('\n')
    for p in range(n_people):
        for i in range(n_week_days):
            csvfile.write(str(random.randint(0,1)))
            for j in range(n_time_slots - 1):
                csvfile.write(',' + str(random.randint(0,1)))
            csvfile.write('\n')
    csvfile.close()

def generateChoreData(filename, n_chores, max_frecuency, max_priority):
    csvfile =  open(filename, 'w')
    csvfile.write('chore, frecuency, priority\n')
    for chore in range(n_chores):
        csvfile.write(str(chore))
        csvfile.write(',' + str(random.randint(1,max_frecuency)))
        csvfile.write(',' + str(random.randint(0,max_priority)))
        csvfile.write('\n')
    csvfile.close()

# generateScheduleData("data/schedules.csv", 2, 6, 6)
# generateChoreData("data/chores.csv", 4, 3, 3)

            
