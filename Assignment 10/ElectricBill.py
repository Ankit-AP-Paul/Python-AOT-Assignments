import re
import matplotlib.pyplot as plt

f = open("bill.txt", mode='r')
s = f.readline()

p = re.compile('\w+')
a = p.findall(s)

months = []
expense = []
for words in a:
    if words.isnumeric():
        expense.append(int(words))
    else:
        months.append(words)
print(expense)
print(months)

plt.bar(x=months, height=expense)
plt.title('Electricity Bill')
plt.xlabel('Months --->')
plt.ylabel('Monthly Bill --->')
plt.grid(axis='y')
plt.show()
f.close()
