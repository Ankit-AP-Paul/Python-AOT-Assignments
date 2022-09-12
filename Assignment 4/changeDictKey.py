d = { "name": "Kelly",  "age":25,  "salary": 8000,  "city": "New York"}
k=list(d.keys())
v=list(d.values())
i=k.index('city')
d.pop('city')
d['location']=v[i]
print("Modified dictionary = ",d)