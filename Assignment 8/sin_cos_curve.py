import numpy as np
import matplotlib.pyplot as plt

time = np.arange(0, 4*np.pi, 0.1)
choice = int(input('Enter 1 for SIN curve or 2 for COS curve = '))
if choice == 1:
    amp = np.sin(time)
    plt.plot(time, amp)
    plt.title("Sin Curve")
else:
    amp = np.cos(time)
    plt.plot(time, amp)
    plt.title("Cos Curve")
plt.xlabel('Time --->')
plt.ylabel('Amplitude --->')
plt.grid(True, which='both')
plt.axhline(y=0, color='0')
plt.show()
