def unique(a):
    b=[]
    for i in a:
        if i not in b:
            b.append(i)
    return b

a=list(map(int,input("Enter the numbers in the list = ").split()))
b=unique(a)
print("Original List = ",a)
print("List with unique elements = ",b)
