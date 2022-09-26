from numpy import random

a = random.randint(100,size=(3, 3))    #create a matrix of random elements from 0-100
print('Random 3*3 Matrix = ')
print(a)

sum=0
for i in range(3):
    for j in range(3):
        if i==j:
            sum+=a[i][j]

print('Sum of diagonal elements = ',sum)