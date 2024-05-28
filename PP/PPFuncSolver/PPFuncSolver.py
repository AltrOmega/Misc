from scipy.optimize import fsolve
from sympy import symbols, lambdify, sympify
import numpy as np
import matplotlib.pyplot as plt

def create_function(user_input):
    x = symbols('x')
    expression = sympify(user_input)
    func = lambdify(x, expression, 'numpy')
    return func

def plot_functions_and_intersection(f, g, roots):
    x_values = np.linspace(min(roots) - 5, max(roots) + 5, 400)
    y_values_f = f(x_values)
    y_values_g = g(x_values)

    plt.figure(figsize=(8, 6))
    plt.plot(x_values, y_values_f, label='f(x)')
    plt.plot(x_values, y_values_g, label='g(x)')

    for root in roots:
        plt.plot(root, f(root), 'ro')

    plt.legend()
    plt.grid(True)
    plt.axhline(y=0, color='black', linewidth=1.5)
    plt.axvline(x=0, color='black', linewidth=1.5)
    plt.xlabel('X Axis')
    plt.ylabel('Y Axis')
    plt.title('Intersection of Two Functions')

    plt.show()

user_input = input("Podaj pierwszą funkcję (domyślnie: x**2): ")
user_input = "x**2" if user_input == "" else user_input
g = create_function(user_input)

user_input = input("Podaj drugą funkcję (domyślnie: x*2-1): ")
user_input = "x*2-1" if user_input == "" else user_input
f = create_function(user_input)


user_input = input("Podaj punkt lub punkty startowe po przecinku (domyślnie: -100): ")
user_input = "-100" if user_input == "" else user_input
print(user_input)

initial_guess = [float(num) for num in user_input.split(",")]

def h(x):
    return f(x) - g(x)

roots = fsolve(h, initial_guess, maxfev=100000, xtol=1e-12, epsfcn=0.01)

tolerance = 1e-10

for root in roots:
    if np.abs(f(root) - g(root)) < tolerance:
        print(f"Intersection found at x = ~{root} is valid.")
    else:
        print(f"Intersection found at x = ~{root} may not be valid.")

print(f"Corresponding y-values are ~{[f(x) for x in roots]}")

plot_functions_and_intersection(f, g, roots)