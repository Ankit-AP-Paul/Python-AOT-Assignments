s=input("Enter the string = ")
max=0
for i in range(len(s)):
    count=1
    for j in range(i+1,len(s)):
        if s[i]==s[j]:
            count+=1
    if max<count:
        max=count
print("Neighbour of maximum length = ",max)