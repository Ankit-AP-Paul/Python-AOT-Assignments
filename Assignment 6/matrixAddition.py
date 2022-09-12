import numpy as np

a=[]
for i in range(3):
    print('Enter the row of 3 elements in Matrix 1 = ',end='')
    r=list(map(int,input().split()))
    a.append(r)
x=np.array(a)
print()

a=[]
for i in range(3):
    print('Enter the row of 3 elements in matrix 2 = ',end='')
    r=list(map(int,input().split()))
    a.append(r)
y=np.array(a)
print()

print('Matrix 1 = ')
print(x)
print('Matrix 2 = ')
print(y)
print('Sum = ')
print(np.add(x,y))