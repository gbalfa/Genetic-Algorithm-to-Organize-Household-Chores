"""
Data visualization
"""


def print_timetable(house_chores, chromosome):
    weekDays = ("Monday              ","Tuesday             ","Wednesday           ","Thursday            ","Friday              ","Saturday            ")
    for elem in weekDays:
        print(elem, ' | ', end='')
    print()
    lista_nombres = []
    i = 0
    while i < 6: # time slots per day
        j = 0
        while j < 6: # week days
            flag = False
            k = 0
            while k < len(chromosome):
                if chromosome[k][0] == j + 1 and chromosome[k][1] == i + 1:
                    flag = True
                    lista_nombres.append(house_chores[k % len(house_chores)][0])
                    chore_name = house_chores[k % len(house_chores)][0]
                    p = chromosome[k][2]
                k = k + 1
            if flag:
                if len(chore_name) < 20:
                    chore_name = chore_name + ' ' + str(p) + ' '  + (17 - len(chore_name)) * ' '
                print(chore_name, ' | ', end='')
            else:
                print('                    ', ' | ', end='')
            j = j + 1
        print()
        i = i + 1
    print(lista_nombres)

            
