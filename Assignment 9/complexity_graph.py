from math import factorial, log
import matplotlib.pyplot as plt

N = int(input("Enter N = "))

a = []
b = []
c = []
d = []
e = []
f = []
g = []
h = []
n = []
for i in range(1, N + 1, ):
    a.append(factorial(i))
    b.append(2 ** i)
    c.append(i ** 3)
    d.append(i ** 2)
    e.append(i * log(i))
    f.append(i)
    g.append(log(i))
    h.append(1)
    n.append(i)

plt.plot(n, a)
plt.plot(n, b)
plt.plot(n, c)
plt.plot(n, d)
plt.plot(n, e)
plt.plot(n, f)
plt.plot(n, g)
plt.plot(n, h)
plt.title('Time Complexity')
plt.xlabel('Input Size --->')
plt.ylabel('CPU Operations --->')
plt.legend(['n!', '2^n', 'n^3', 'n^2', 'n log(n)', 'n', 'log(n)', '1'], loc='upper left')
plt.grid()
plt.show()
