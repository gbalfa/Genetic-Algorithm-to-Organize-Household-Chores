import guided_creep_mutation as gcm
from file_handler import arrangeSchedules, readCSV

week_days = 6
# Representation of availability in time slots P X (D X T)
schedules = arrangeSchedules(readCSV("data/schedules.csv"), week_days)
p = len(schedules)

# Chores (recurrence/week)
# chores = [['Limpiar baño', 2], ['Barrer patio', 2], ['Limpiar vidrios', 3]]
chores = readCSV("data/chores.csv")
print(chores)
print(schedules)

# DTP
# varbound = [[1, 6], [1, 6], [1, p]]

# # model run
# gcm.ga(dimension=3, varbound=varbound, schedules=schedules, house_chores=house_chores)


