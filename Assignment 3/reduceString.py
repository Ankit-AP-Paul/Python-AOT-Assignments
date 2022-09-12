s=input("Enter a string =  ")
s1=""
for i in s:
    c=s.count(i) # counting the frequency of each character
    if c%2==1 and i not in s1:
            s1=s1+i
if s1=="":
    print("Empty string")
else:
    print("New string = ",s1)
