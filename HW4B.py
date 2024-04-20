# @source: https://github.com/lihiSabag/Numerical-Analysis-2023.git
import math

def trapezoidalIntegral(f, a, b, n):
    h = (b - a) / n
    T = f(a) + f(b)
    integral = 0.5 * T  # Initialize with endpoints
    for i in range(1, n):
        x_i = a + i * h
        integral += f(x_i)
    integral *= h
    return integral

if __name__ == '__main__':
    f = lambda x: (math.sin(x))
    result = trapezoidalIntegral(f, 0, math.pi, 4)
    print("Approximate integral:", round(result,5))
