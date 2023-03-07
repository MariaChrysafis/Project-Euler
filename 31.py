import numpy as np
arr = [1, 2, 5, 10, 20, 50, 100, 200]
p = np.polynomial.Polynomial([1])
for x in arr :
    poly = [0] * 201
    poly[0] = 1
    val = x
    while val <= 200 :
        poly[val] = 1
        val += x
    get_poly = np.polynomial.Polynomial(poly)
    p = np.polynomial.polynomial.polymul(get_poly, p)
print(np.polyval(p, 200))
