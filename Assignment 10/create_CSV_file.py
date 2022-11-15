import  csv
import random

f=open('marks.csv',mode='w',newline='')
csv_writer=csv.writer(f)
csv_writer.writerow(['English', 'Maths', 'Science', 'Computer'])
for i in range(10):
    csv_writer.writerow([random.randint(0,100),random.randint(0,100),random.randint(0,100),random.randint(0,100)])
print('CSV file created')
f.close()