# @source: https://github.com/lihiSabag/Numerical-Analysis-2023.git
import sympy as sp
def newton_raphson(polynomial, interval, epsilon=0.0001):
    print("Newton Raphson method")
    x = sp.symbols('x')
    f = sp.sympify(polynomial)
    df = sp.diff(f, x)
    df_func = sp.lambdify(x, df)
    p0 = (interval[0] + interval[1]) / 2
    if df_func(p0) == 0:
        print("Derivative is zero at p0, method cannot continue.")
        return None  # Return None if derivative is zero
    print("{:<10} {:<15} {:<15} ".format("Iteration", "po", "p1"))
    for i in range(100):
        if df_func(p0) == 0:
            print("Derivative is zero at p0, method cannot continue.")
            return None  # Return None if derivative is zero
        p = p0 - f.subs(x, p0) / df_func(p0)
        if abs(p - p0) < epsilon:  # Check if difference between p and p0 is below epsilon
            return p, i # Procedure completed successfully
        print("{:<10} {:<15.9f} {:<15.9f} ".format(i, p0, p))
        p0 = p
    print("Method did not converge within 100 iterations.")
    return None

def secant_method(polynomial, interval, epsilon=0.0001):
    print("Secant method")
    x = sp.symbols('x')
    f = sp.sympify(polynomial)
    func = sp.lambdify(x, f)
    a, b = interval
    if func(b) - func(a) == 0:
        print("Method cannot continue.")
        return
    print("{:<10} {:<15} {:<15} {:<15}".format("Iteration", "x0", "x1", "p"))
    for i in range(100):
        if func(b) - func(a) == 0:
            print("Method cannot continue.")
            return
        p = a - func(a) * ((b - a) / (func(b) - func(a)))
        if abs(p - b) < epsilon:
            return p, i  # Procedure completed successfully
        print("{:<10} {:<15.6f} {:<15.6f} {:<15.6f}".format(i, a, b, p))
        a = b
        b = p
    print("Method did not converge within 100 iterations.")
    return None

if __name__ == '__main__':
    polynomial = 'x**2 - 5*x + 2'
    interval = (0, 10)
    epsilon = 0.0001
    root, numberOfIteration = newton_raphson(polynomial, interval, epsilon)
    if root is not None:
        print("In the Newton Raphson method, the number of iterations performed is", numberOfIteration)
        print("The equation f(x) has an approximate root at x = {:<15.9f} ".format(root),"\n")
    root, numberOfIteration = secant_method(polynomial, interval, epsilon)
    if root is not None:
        print("In the Secant method, the number of iterations performed is", numberOfIteration)
        print("The equation f(x) has an approximate root at x = {:<15.9f} ".format(root),"\n")
