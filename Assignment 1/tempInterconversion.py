ch=int(input('Enter 1 to convert celcius to farenheit and 2 to convert farenheit to celcius = '))
if ch==1:
    c=float(input('Enter temperature in Celcius = '))
    f=(9*c/5)+32
    print('Temperature in Farenheit = ',f)
elif ch==2:
    f=float(input('Enter temperature in farenheit = '))
    c=(f-32)*5/9
    print('Temperature in celcius = ',c)
else:
    print('Wrong choice')