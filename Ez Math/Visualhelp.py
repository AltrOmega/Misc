import numpy as np
import matplotlib.pyplot as plt

def func(x):
    return (1/4)*x**4 - x**3 - 2*x**2 + 12*x - 5

def derivative(x):
    return x**3 - 3*x**2 - 4*x + 12

x = np.linspace(-4, 5, 4000000)

y = func(x)
y_prime = derivative(x)

plt.figure(figsize=(10, 5))
plt.plot(x, y, label='Function f(x)')
plt.plot(x, y_prime, label="f'(x) - Derivative", linestyle='--')
plt.title("Function and its Derivative")
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
plt.legend()
plt.show()
