from itertools import combinations, permutations
a=list(map(int,input("Enter the list = ").split()))
b=int(input("Enter the length = "))
p=permutations(a,b)
print("Permutations are = ",list(p))
c=combinations(a,b)
print("Combinations are = ",list(c))
