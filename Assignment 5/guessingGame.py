import random
a=[]
while(True):
    s=input("Enter a 5 letter word = ")
    if s!="###" :
        if len(s)==5:
            a.append(s.lower())
    else:
        break
word=random.choice(a)
n=int(input("Enter the number of guesses = "))
for i in range(n):
    s2=""
    s1=input("Enter the guess word = ")
    s1=s1.lower()
    ch=0
    if s1!=word:
        for j in s1:
            if j in word:
                s2=s2+j
            else:
                s2=s2+'.'
        print(s2)
    else:
        print("Correct guess")
        ch=1
        break
    a.remove(s1)
if ch==0:
    print("Possible words = ")
    s3=""
    for i in s2:
        if(i!='.'):
            s3=s3+i
    for i in a:
        k=0
        for j in s3:
            if j in i:
                k+=1
        if k==len(s3) :
            print(i.upper())
