import csv
import matplotlib.pyplot as plt

f = open('marks.csv', mode='r')
csv_reader = csv.reader(f)

sub = ['Eng', 'Maths', 'Sci', 'Comp']
avgMarks=[]
eng = []
maths = []
sci = []
comp = []

for line in csv_reader:
    if line[0].isnumeric():
        eng.append(int(line[0]))
        maths.append(int(line[1]))
        sci.append(int(line[2]))
        comp.append(int(line[3]))

avgMarks.append(sum(eng)/len(eng))
avgMarks.append(sum(maths)/len(maths))
avgMarks.append(sum(sci)/len(sci))
avgMarks.append(sum(comp)/len(comp))

plt.subplot(1,2,1)
plt.bar(x=sub, height=avgMarks)
plt.title('Bar Graph')
plt.xlabel('Subject --->')
plt.ylabel('Average Marks --->')
plt.grid(axis='y')

plt.subplot(1,2,2)
plt.pie(avgMarks, labels=sub)
plt.title('Pie Chart')

plt.suptitle('Average Mars in each subject')
plt.show()