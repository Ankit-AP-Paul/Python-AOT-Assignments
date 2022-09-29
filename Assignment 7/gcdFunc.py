def calcGCD(a,b):
    if a>b:
        return(calcGCD(a-b,b))
    elif a<b:
        return(calcGCD(a,b-a))
    else:
        return a

try:
    a,b=list(map(int,input("Enter two numbers = ").split()))
    if a<0 or b<0:
        raise Exception
    print("GCD of ",a," and ",b," = ",calcGCD(a,b))
except:
    print("Exception occured")