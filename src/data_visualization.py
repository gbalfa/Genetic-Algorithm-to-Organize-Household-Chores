"""
Data visualization
"""

import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def greatestMultipleOf(x, n):
    day = 0
    i = 1
    m = x * i
    while m <= n:
        day += 1
        i += 1
        m = x * i
    return day


def heatMapsFromCromosome(X, n_week_days, n_time_slots_day, size_event_chunk, schedule_fields, schedules):
    rows = []
    events_per_person = [0] * len(schedules)
    week_days = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat']
    # decode [timeSlot, persona] => [weekday, slot]
    for i in range(0, len(X), size_event_chunk):
        timeSlot = X[i]
        person = X[i + 1]
        events_per_person[int(person)] += 1
        rows.append([greatestMultipleOf(n_time_slots_day, timeSlot),
                    timeSlot % n_time_slots_day])
    matrix = np.zeros((n_week_days, n_time_slots_day))
    for elem in rows:
        matrix[int(elem[0])][int(elem[1])] += 1

    # disponibilidad
    schedules_sum = [0] * n_week_days * n_time_slots_day
    for schedule in schedules:
        for i_timeSlot in range(len(schedule)):
            if schedule[i_timeSlot]:
                schedules_sum[i_timeSlot] += 1

    mtx_schedules = np.zeros((n_week_days, n_time_slots_day))

    for i_timeSlot in range(len(schedules_sum)):
        mtx_schedules[greatestMultipleOf(
            n_time_slots_day, i_timeSlot)][i_timeSlot % n_time_slots_day] += schedules_sum[i_timeSlot]

    df1 = pd.DataFrame(matrix, columns=schedule_fields,
                       index=week_days[:n_week_days])
    df2 = pd.DataFrame(mtx_schedules, columns=schedule_fields,
                       index=week_days[:n_week_days])
    data_events_per_person = {'personas': [str(i) for i in range(
        len(events_per_person))], 'cantidad eventos asignados': events_per_person}
    df3 = pd.DataFrame(data_events_per_person)

    f, axs = plt.subplots(1, 3)
    sns.heatmap(df1, ax=axs[0]).set_title('Asignaciones de tareas')
    sns.heatmap(df2, ax=axs[1]).set_title('Horarios disponibles')
    sns.barplot(data=df3, x='personas',
                y='cantidad eventos asignados', ax=axs[2])
    f.tight_layout()
    plt.show()
    return rows
