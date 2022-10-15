import random
import numpy as np
import matplotlib.pyplot as plt

bill = []
for i in range(12):
    bill.append(random.randint(500, 2000))
month = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

bill = np.array(bill)
month = np.array(month)
choice = int(input('Enter 1 for line graph, 2 for bar graph or 3 for pie chart = '))
if choice == 1:
    plt.plot(month, bill)
    plt.xlabel('Months --->')
    plt.ylabel('Monthly Bill --->')
    plt.grid(True)
elif choice == 2:
    plt.bar(month, bill)
    plt.xlabel('Months --->')
    plt.ylabel('Monthly Bill --->')
    plt.grid(axis='y')
else:
    plt.pie(bill, labels=month)
plt.title('Electricity Bill')
plt.show()
