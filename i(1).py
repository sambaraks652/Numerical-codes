import numpy as np

def lagrange_interpolation(x, y):
    def L(k, x_val):
        """Calculate the k-th Lagrange basis polynomial L_k(x) at x_val."""
        out = [(x_val - x[j]) / (x[k] - x[j]) for j in range(len(x)) if j != k]
        return np.prod(out)
    
    def P(x_val):
        """Calculate the polynomial P(x) using the Lagrange basis polynomials."""
        return sum(y[k] * L(k, x_val) for k in range(len(x)))
    
    # Compute the coefficients of the Lagrange polynomial
    def lagrange_poly_coeffs(x, y):
        """Generate polynomial coefficients for Lagrange interpolation."""
        degree = len(x) - 1
        coeffs = np.zeros(degree + 1)
        for k in range(len(x)):
            p_coeffs = np.poly1d([1])
            for j in range(len(x)):
                if j != k:
                    p_coeffs *= np.poly1d([1, -x[j]]) / (x[k] - x[j])
            coeffs += y[k] * p_coeffs.coefficients
        return coeffs

    coeffs = lagrange_poly_coeffs(x, y)
    return coeffs

x = [1, 2, 3, 4]
y = [1, 4, 9, 16]
coeffs = lagrange_interpolation(x, y)
print("Lagrange polynomial coefficients:", coeffs)
