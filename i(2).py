def newton_divided_difference(x, y):
    n = len(x)
    coeffs = y.copy()
    
    for j in range(1, n):
        for i in range(n-1, j-1, -1):
            coeffs[i] = (coeffs[i] - coeffs[i-1]) / (x[i] - x[i-j])
    
    return coeffs

def newton_interpolation(x, y):
    coeffs = newton_divided_difference(x, y)
    
    def P(x_new):
        n = len(x)
        p = coeffs[n-1]
        for k in range(n-2, -1, -1):
            p = p * (x_new - x[k]) + coeffs[k]
        return p
    
    return P


x = [1, 2, 3, 4]
y = [1, 4, 9, 16]
P = newton_interpolation(x, y)
print("Newton's interpolation at x=2.5:", P(2.5))