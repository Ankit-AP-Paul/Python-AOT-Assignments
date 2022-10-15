arr=list(map(int,input("Enter the numbers in the list = ").split()))
num=int(input("Enter the number to be inserted = "))
newArr=[]
for i in range(len(arr)+1):
    temp=list(arr)
    temp.insert(i,num)
    newArr.append(temp)
print("New List = ",newArr)