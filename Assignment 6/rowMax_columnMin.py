import numpy as np

a=[]
for i in range(3):
    print('Enter the row of 3 elements = ',end='')
    r=list(map(int,input().split()))
    a.append(r)
x=np.array(a)

print('Maxtrix = ')
print(x)
print('Row wise maximum elements = ',np.amax(x,axis=1))         #row axis = 1
print('Column wise minimum elements = ',np.amin(x,axis=0))      #column axis = 0