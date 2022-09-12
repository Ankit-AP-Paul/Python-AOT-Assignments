d1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30} 
d2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
k=list(d2.keys())
v=list(d2.values())
for i in range(len(k)):
    d1[k[i]]=v[i]
print("Merged Dictionary = ",d1)