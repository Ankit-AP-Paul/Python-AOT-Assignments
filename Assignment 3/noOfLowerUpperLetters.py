def counter(s):
    c1, c2 = 0, 0
    for i in s:
        if i.isupper():
            c1 = c1 + 1
        elif i.islower():
            c2 = c2 + 1
    return c1,c2


s = input("Enter a string = ")
lower, upper = counter(s)
print("No. of uppercase letter = ",upper)
print("No. of lowercase letter = ",lower)
