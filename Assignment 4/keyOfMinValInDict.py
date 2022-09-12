from decimal import MAX_EMAX
d = { "name": "Kelly",  "age":25,  "salary": 8000,  "city": "New York"}
k=list(d.keys())
v=list(d.values())
v1=[]
for i in v:
    v1.append(str(i))
min=MAX_EMAX
for i in v1:
    if i.isnumeric() and min>int(i):
        min=int(i)
        id=v1.index(i)
print("Dictionary key having min value = ",k[id])