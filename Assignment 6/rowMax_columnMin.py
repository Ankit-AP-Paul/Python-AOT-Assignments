from numpy import random
import numpy as np

x=random.randint(100,size=(3,3))

print('Maxtrix = ')
print(x)
print('Row wise maximum elements = ',np.amax(x,axis=1))         #row axis = 1
print('Column wise minimum elements = ',np.amin(x,axis=0))      #column axis = 0