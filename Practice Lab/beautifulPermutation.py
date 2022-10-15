from math import log2
from itertools import permutations

n=int(input('Enter the number = '))
if n==2**int(log2(n)):
    print('Not Possible')
else:
    p=list(permutations(range(1,n+1)))
    for i in p:
        c=0
        i=list(i)
        for j in range(len(i)-1):
            if i[j]&i[j+1]>0:
                c+=1
        if c==n-1:
            print(i)
            break