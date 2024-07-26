import numpy as np

def power_iteration(A, num_iterations=1000, tolerance=1e-10):
    n = A.shape[0]
    v = np.random.rand(n)
    v = v / np.linalg.norm(v)
    
    for _ in range(num_iterations):
        Av = A @ v
        eigenvalue = v.T @ Av
        new_v = Av / np.linalg.norm(Av)
        
        if np.allclose(v, new_v, rtol=tolerance):
            break
        
        v = new_v
    
    return eigenvalue, v


A = np.array([[4, 1, 1],
              [1, 3, -1],
              [1, -1, 2]])

eigenvalue, eigenvector = power_iteration(A)
print("Dominant eigenvalue:", eigenvalue)
print("Corresponding eigenvector:", eigenvector)