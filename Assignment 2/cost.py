i=int(input("Enter the no. of items = "))
if i<10:
    c=120*i
elif i>=10 and i<=99:
    c=100*i
else:
    c=70*i
print("Total cost = ",c)
