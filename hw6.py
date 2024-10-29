import numpy as np
import matplotlib.pyplot as plt


#Q1
def sine_wave(x, A, w):
    return A * np.sin(w * x)
x = np.linspace(0, 2 * np.pi, 1000)
A_arr = np.array([1, 3, 4, 8, 12])
w_arr = np.array([4, 5, 12, 23, 35])

for i, (A, w) in enumerate(zip(A_arr, w_arr), start=1):
    y = sine_wave(x, A, w)
    plt.plot(x, y, label = f"sine function {i}")

plt.xlabel("x data")
plt.ylabel("y data")
plt.title("5 Different Sine Functions")
plt.legend()
plt.show()

# Q2
ls1 = np.random.randint(0, 101, 40)
ls2 = np.random.randint(0, 101, 40)
x = np.arange(40)

plt.figure(figsize = (10, 6))
plt.plot(x, ls1, color = 'orange', linewidth = 10, label = "ls1 line")
plt.plot(x, ls2, color = 'red', linestyle = "--", label = "ls2 line")
plt.xlabel("Index")
plt.ylabel("Random Data")
plt.title("Ranom Data Plot")
plt.legend()
plt.show()