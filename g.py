def trapezoidal_rule(f, a, b, n):
    """
    Approximate the integral of f(x) from a to b using the trapezoidal rule with n subintervals.
    
    Parameters:
    f : function
        The integrand.
    a, b : float
        The limits of integration.
    n : int
        The number of subintervals.
        
    Returns:
    float
        The approximate value of the integral.
    """
    h = (b - a) / n
    integral = (f(a) + f(b)) / 2.0
    for i in range(1, n):
        integral += f(a + i * h)
    integral *= h
    return integral

# Example usage:
import math

# Define the function to be integrated
def f(x):
    return math.exp(-x**2)

# Define the limits of integration
a = 0
b = 1

# Define the number of subintervals
n = 100

# Calculate the integral
result = trapezoidal_rule(f, a, b, n)
print(f"The approximate value of the integral is: {result}")
