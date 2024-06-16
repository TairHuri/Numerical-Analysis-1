import numpy as np


def trapezine(func, z_min, z_max, epsilon):
    """
    Perform extended trapezoidal rule to calculate numerical integration.

    Input:
        func: the function to be integrated
        z_min: lower limit of the integration
        z_max: upper limit of the integration
        epsilon: desired accuracy of the integration, e.g., 1e-8.

    Returns:
        new_I: the numerical integration result with desired accuracy.
        err: error of the process O(h^3).
    """
    evaluation = 0
    h = z_max - z_min
    new_I = h * (func(z_max) + func(z_min)) / 2
    relative_accuracy = 1
    evaluation += 2

    while relative_accuracy >= epsilon:
        h /= 2
        z_array = np.arange(z_min, z_max + h, h)
        old_I = new_I
        new_I = old_I / 2 + h * sum(func(z_array[2 * i - 1]) for i in range(1, (len(z_array) - 1) // 2 + 1))
        relative_accuracy = abs((new_I - old_I) / old_I)
        evaluation += len(z_array) // 2 - 1

    err = new_I * 0.5 * relative_accuracy
    print("Number of evaluated terms: ", int(evaluation))
    return new_I, err


def simpson(func, z_min, z_max, epsilon):
    """
    Perform extended Simpson's rule to calculate numerical integration value.

    Input:
        func: the function to be integrated
        z_min: lower limit of the integration
        z_max: upper limit of the integration
        epsilon: desired accuracy of the integration, e.g., 1e-8.

    Returns:
        new_I: the numerical integration result with desired accuracy.
        err: error of the process O(h^5).
    """
    evaluation = 0
    h = z_max - z_min
    T_j = h * (func(z_max) + func(z_min)) / 2
    h /= 2
    z_array = np.arange(z_min, z_max + h, h)
    T_j1 = T_j / 2 + h * sum(func(z_array[2 * t - 1]) for t in range(1, (len(z_array) - 1) // 2 + 1))
    new_I = 4 * T_j1 / 3 - T_j / 3
    relative_accuracy = 1
    evaluation += 3

    while relative_accuracy >= epsilon:
        old_I = new_I
        h /= 2
        z_array = np.arange(z_min, z_max + h, h)
        T_j = T_j1
        T_j1 = T_j / 2 + h * sum(func(z_array[2 * t - 1]) for t in range(1, (len(z_array) - 1) // 2 + 1))
        new_I = 4 * T_j1 / 3 - T_j / 3
        relative_accuracy = abs((new_I - old_I) / old_I)
        evaluation += len(z_array) // 2

    err = new_I * 0.5 * relative_accuracy
    print("Number of evaluated terms: ", int(evaluation))
    return new_I, err


def main():
    func = lambda x: np.sin(x)
    z_min = 0
    z_max = np.pi
    epsilon = 1e-8

    trapezine_result, trapezine_err = trapezine(func, z_min, z_max, epsilon)
    print(f"Trapezine Rule: Integral = {trapezine_result}, Error = {trapezine_err}")

    simpson_result, simpson_err = simpson(func, z_min, z_max, epsilon)
    print(f"Simpson's Rule: Integral = {simpson_result}, Error = {simpson_err}")


if __name__ == "__main__":
    main()

