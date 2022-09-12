t = (11, [22, 33], 44, 55)
for i in range(len(t)):
    if type(t[i]) is list:
        t[i][0]=222
print("Modified tuple = ",t)