n=int(input("Enter the number"))
print("palindrome numbers are = ")
for i in range(n):
    rev=int(str(i)[::-1]) #reverse of a number
    if i==rev:
        print(i)
