def pangramCheck(s):
    s1 = "abcdefghijklmnopqrstuvwxyz"
    for i in s1:
        if i not in s:
            return -9999
    return 1


s=input("Enter a string = ")
ck=pangramCheck(s.lower())
if ck==1:
    print("Pangram")
else:
    print("Not a pangram")