# @source: https://github.com/lihiSabag/Numerical-Analysis-2023.git
import sympy as sp
from sympy import sympify

def newton_raphson(polynomial, interval, epsilon):
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

def secant_method(polynomial, interval, epsilon):
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

def get_polynomial_from_user():
  """
  This function prompts the user to enter a polynomial function as a string
  and returns a sympy expression.
  """
  while True:
    polynomial_str = input("Enter the polynomial function (e.g., x**2 - 3*x + 2): ")
    try:
      x = sp.symbols('x')
      polynomial_func = sp.sympify(polynomial_str)
      return polynomial_func
    except SyntaxError:
      print("Invalid polynomial format. Please try again.")

if __name__ == '__main__':
    polynomial = get_polynomial_from_user()
    # Get interval from user input
    flag = 'no'
    while flag == 'no':
        interval_start = float(input("Enter the start of the interval: "))
        interval_end = float(input("Enter the end of the interval: "))
        if interval_end > interval_start:
            flag = 'yes'
        else:
            print("Invalid, lease try again.")
    interval = (interval_start, interval_end)
    epsilon = 0.0001
    method_choice = float(input("Enter '1' for Newton-Raphson method or '2' for Secant method: "))
    while method_choice != 1 and method_choice != 2:
        print("Invalid, lease try again.")
        method_choice = float(input("Enter '1' for Newton-Raphson method or '2' for Secant method: "))
    if method_choice == 1:
        root, numberOfIteration = newton_raphson(polynomial, interval, epsilon)
        if root is not None:
            print("In the Newton Raphson method, the number of iterations performed is", numberOfIteration)
            print("The equation f(x) has an approximate root at x = {:<15.9f} ".format(root),"\n")
    else:
        root, numberOfIteration = secant_method(polynomial, interval, epsilon)
        if root is not None:
            print("In the Secant method, the number of iterations performed is", numberOfIteration)
            print("The equation f(x) has an approximate root at x = {:<15.9f} ".format(root),"\n")
