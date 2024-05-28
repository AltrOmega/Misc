from sympy import symbols, solve

x = symbols('x')

equation = 2*x+3

result = solve(equation, x)

print(result)