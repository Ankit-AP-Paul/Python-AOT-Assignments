try:
    a,b=list(map(int,input("Enter two numbers = ").split()))
    ch=input("1.Add 2.Subtract 3.Multiply 4.Division 5.Exponent\nEnter your choice = ")
    if ch=='1':
        print("Sum = ",a+b)
    elif ch=='2':
        print("Difference = ",a-b)
    elif ch=='3':
        print("Product = ",a*b)
    elif ch=='4':
        print("Quotient = ",a//b)
        print("Remainder = ",a%b)
    elif ch=='5':
        print("Value = ",a**b)
    else:
        print("Wrong choice")
except TypeError:
    print("Type Error has occured")
except ArithmeticError:                     #Division by zero error falls in ArithmeticError
    print("Arithmetic error has occured")
except ValueError:
    print("Value Error has occured")
except:
    print("Error occured")