p=int(input('Enter principal amount = '))
r=float(input('Enter rate of interest = '))
t=float(input('Enter time = '))
si=(p*r*t)/100
print('Amount payable after SI = ',si)
amt_ci=p*(1+r/100)**t
print('Amount payable after CI = ',amt_ci)