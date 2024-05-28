from sympy import symbols, diff, solve

x = symbols('x')

def find_monotonicity_extrema_and_print(func):
    f_prime = diff(func, x)

    critical_points = solve(f_prime, x)

    test_points = sorted(critical_points + [min(critical_points) - 1, max(critical_points) + 1])

    intervals = []
    extrema = []

    for i in range(len(test_points) - 1):
        mid_point = (test_points[i] + test_points[i + 1]) / 2
        if f_prime.subs(x, mid_point) > 0:
            monotonicity = "rosnąca"
        elif f_prime.subs(x, mid_point) < 0:
            monotonicity = "malejąca"
        else:
            monotonicity = "stała"
        intervals.append(f"({test_points[i]}, {test_points[i + 1]}) - {monotonicity}")

    for cp in critical_points:
        if f_prime.subs(x, cp - 0.1) * f_prime.subs(x, cp + 0.1) < 0:
            extrema_type = "minimum" if f_prime.subs(x, cp + 0.1) > 0 else "maksimum"
            extrema.append((cp, extrema_type))

    print("Przedziały monotoniczności funkcji:")
    for interval in intervals:
        print(interval)
    
    print("\nEkstrema funkcji:")
    for extremum in extrema:
        point, extrema_type = extremum
        print(f"{extrema_type.capitalize()} lokalne w punkcie x = {point}")

new_func = -4**4 -4*x**3+8*x**2
find_monotonicity_extrema_and_print(new_func)
