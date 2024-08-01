import math
import itertools
from math import gcd

import more_itertools
import numpy as np
from more_itertools import distinct_permutations
mod = 83456729
n = 34
def brute () :
    p = []
    for i in range(n - 1) :
        p.append(i + 2)
    ans = 0
    for arr in itertools.permutations(p) :
        okay = True
        for i in range(1, len(arr)) :
            if gcd(arr[i], arr[i - 1]) != 1 :
                okay = False
        ans += okay
    return ans
def reduce (x: int) -> int :
    found = False
    for i in range(1, n + 1) :
        if gcd(x, i) != 1 and x != i:
            found = True
    if not found :
        return 1
    for i in range(2, x + 1) :
        while x % (i * i) == 0 :
            x //= i
    return x

oc = [0] * (n + 1)
ps = set()
for ind in range(1, n + 1) :
    # print(reduce(i))
    print(ind, reduce(ind))
    ps.add(reduce(ind))
    oc[reduce(ind)] += 1

prod_arr = [0] * (n + 1)
for ind in range(n + 1) :
    prod_arr[ind] = 1
    for j in range(ind + 1, n + 1) :
        prod_arr[ind] *= oc[j] + 1

res = prod_arr[0]
dp = [0] * res


def to_int (arr: list[int]) :
    ans = 0
    for i in range(len(arr)) :
        ans += prod_arr[i] * arr[i]
    return ans

def to_list (x: int) :
    ans = []
    for i in range(len(oc)) :
        a = 0
        while x >= prod_arr[i] != 0:
            x -= prod_arr[i]
            a += 1
        ans.append(a)
    return ans

print(res)
dp = []
for i in range(n + 1) :
    print(i, res)
    dp.append([0] * (res + 1))
print("DONE")
ll = [0] * len(oc)
ll[1] = 1
dp[1][to_int(ll)] = 1
g = []
for i in range(n + 1) :
    g.append([])
    for j in range(n + 1) :
        if gcd(i, j) == 1 :
            g[-1].append(j)
for mask in range(len(dp[0])) :
    arr = to_list(mask)
    for prev in range(len(dp)) :
        if dp[prev][mask] == 0 :
            continue
        for i in g[prev] :
            if arr[i] + 1 <= oc[i] :
                dp[i][mask + prod_arr[i]] += dp[prev][mask]
                if dp[i][mask + prod_arr[i]] >= mod :
                    dp[i][mask + prod_arr[i]] -= mod

ans = 0
for i in range(len(dp)) :
    ans += dp[i][res - 1]
for i in range(len(oc)) :
    if i == 1 :
        oc[i] -= 1
    ans *= math.factorial(oc[i])
print(ans)
