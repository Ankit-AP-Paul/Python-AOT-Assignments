from numpy import random
import numpy as np

a=random.randint(100,size=(3,3))
b=random.randint(100,size=(3,3))

print('Matrix 1 = ')
print(a)
print('Matrix 2 = ')
print(b)
print('Sum = ')
print(np.add(a,b))