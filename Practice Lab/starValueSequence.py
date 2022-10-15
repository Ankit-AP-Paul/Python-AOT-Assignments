arr=list(map(int,input("Enter the list of elements = ").split()))
max=0
for j in range(len(arr)-1):
    count=0
    for i in range(j+1,len(arr)):
        if arr[j]%arr[i]==0:
            count+=1
    if max<count:
        max=count
print("Maximum star value = ",max)