from math import sqrt

def prime(n):
    c=0
    for i in range(1,n+1):
        if n%i==0:
            c=c+1
    if c==2:
        print("Prime No.")
    else:
        print("Not prime")

n=int(input("Enter the number = "))
s=sqrt(n)
if s-int(s)==0:
    prime(int(s))
else:
    print("Not possible")
