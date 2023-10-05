# pi(m * n) = lcm(pi(m), pi(n)) = 120
# decompose into appropriately small m and n
# assume WLOG that m < n
from sympy import *
import pandas

# 2, 3, 5, 11, 31, 41, 61, 709, 2521, 8969, 336419
arr = [[1, 2, 4, 8, 16], [1, 3, 9], [1, 5], [1, 11], [1, 31], [1, 41], [1, 61], [1, 709], [1, 2521], [1, 8969], [1, 336419]]
def get_picano_period(n) :
    if n == 1 :
        return 1
    c = [1, 1];
    a = []
    while not (c in a) :
        a.append(c)
        c = [c[1], (c[0] + c[1]) % n]
    return len(a)

def gcd (a: int, b: int) -> int :
    if a == 0 or b == 0 :
        return max(a, b)
    return gcd(max(a, b) % min(a, b), min(a, b))
def lcm (a: int, b: int) -> int :
    return a * b//gcd(a, b)

d = dict()
for x in arr :
    for y in x :
        d[y] = get_picano_period(y)
def get_arr (x: int, prod: int, period: int) -> int :
    assert period != 0
    if period > 120 or prod > int(1e9) :
        return 0
    if x == len(arr) :
        if period == 120 :
            return prod
        return 0
    return sum(get_arr(x + 1, prod * j, lcm(period, d[j])) for j in arr[x])

print(get_arr(0, 1, 1))
