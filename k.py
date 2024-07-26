import numpy as np

def gradient_descent(f, grad_f, initial_guess, learning_rate=0.1, num_iterations=1000, tolerance=1e-6):
    x = initial_guess
    
    for _ in range(num_iterations):
        gradient = grad_f(x[0], x[1])
        new_x = x - learning_rate * gradient
        
        if np.linalg.norm(new_x - x) < tolerance:
            break
        
        x = new_x
    
    return x, f(x[0], x[1])

# Define the function and its gradient
def f(x, y):
    return x**2 + y**2 - x*y + x - y + 1

def grad_f(x, y):
    return np.array([2*x - y + 1, 2*y - x - 1])


initial_guess = np.array([0, 0])

result, min_value = gradient_descent(f, grad_f, initial_guess)

print("Minimum point:", result)
print("Minimum value:", min_value)