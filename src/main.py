import guided_creep_mutation as gcm

# Representation of availability in time slots P X (D X T)
availability = [[0, 1, 1, 0 , 0, 0], [0, 0, 1, 1, 0, 0]]
p = 2

# House chores (recurrence/week)
house_chores = [['Limpiar baño', 2], ['Barrer patio', 2], ['Limpiar vidrios', 1]]

# DTP
varbound = [[1, 6], [1, 6], [1, p]]

# model run
gcm.ga(dimension=3, varbound=varbound, availability=availability, house_chores=house_chores)


