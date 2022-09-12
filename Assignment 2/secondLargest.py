n=int(input("Enter the size = "))
a=[]
print("Enter the numbers = ")
for i in range(n):
    a.append(int(input()))
print("List = ",a)
a.sort()
print("Second largest number = ",a[-2])
