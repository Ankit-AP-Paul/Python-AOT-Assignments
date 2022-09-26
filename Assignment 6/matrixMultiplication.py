from numpy import random
import numpy as np

x=random.randint(10,size=(3,3))
y=random.randint(10,size=(3,3))

print('Matrix 1 = ')
print(x)
print('Matrix 2 = ')
print(y)
print('Matrix multiplication = ')
print(np.matmul(x,y))