import random
import numpy as np
import matplotlib.pyplot as plt

x = []
for i in range(30):
    x.append(random.randint(0, 100))

y = []
for i in range(30):
    y.append(random.randint(0, 100))

x = np.array(x)
y = np.array(y)
plt.scatter(x, y)
plt.title('Random 2d points')
plt.xlabel('X --->')
plt.ylabel('Y --->')
plt.grid(True, which='both')
plt.show()
