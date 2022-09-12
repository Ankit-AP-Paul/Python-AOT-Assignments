def maximum(a,max,i):
    if i==len(a):
        return max
    else:
        if max<a[i]:
            max=a[i]
        return(maximum(a,max,i+1))

a=list(map(int,input("Enter the list elements = ").split()))
print("List = ",a)
print("Maximum element = ",maximum(a,-9999,0))
