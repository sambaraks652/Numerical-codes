import numpy as np

def qr_algorithm(A, num_iterations=1000):
    n = A.shape[0]
    Q = np.eye(n)
    
    for _ in range(num_iterations):
        Q_k, R_k = np.linalg.qr(A)
        A = R_k @ Q_k
        Q = Q @ Q_k
    
    eigenvalues = np.diag(A)
    eigenvectors = Q
    
    return eigenvalues, eigenvectors


A = np.array([[4, 1, 1],
              [1, 3, -1],
              [1, -1, 2]])

eigenvalues, eigenvectors = qr_algorithm(A)
print("Eigenvalues:", eigenvalues)
print("Eigenvectors:")
print(eigenvectors)