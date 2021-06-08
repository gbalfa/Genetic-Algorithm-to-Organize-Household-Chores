# versión 0.0

import numpy as np
from geneticalgorithm import geneticalgorithm as ga

# representation of availability in time slots 
s1 = [[0, 1, 1, 0 , 0], [0, 0, 1, 1, 0]]

def f(X):
    costo = 0
    if (np.sum(X[:5]) != 1):
       costo = costo + 100 
    if (np.sum(X[5:]) != 1):
       costo = costo + 100 
    i = 0
    while (i < 5):
        if (X[i] == 1 and s1[0][i] == 0):
            costo = costo + 100
        i = i + 1
    i = 5
    j = 0
    while (i < 10):
        if (X[i] == 1 and s1[1][j] == 0):
            costo = costo + 100
        i = i + 1
        j = j + 1
    i = 0
    j = 5
    while (i < 5):
        if(X[i] != X[j]):
            costo = costo + 100
        i = i + 1 
        j = j + 1 
    return costo

# one event, 5 slots and 2 person => 10 bits
model=ga(function=f,dimension=10,variable_type='bool')

model.run()
#print(model.param)
