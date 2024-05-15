import math
import random
import matplotlib.pyplot as plt
import numpy as np
def xor_product (a: int, b: int) -> int :
    if a == 0 or b == 0 :
        return 0
    l = math.floor(math.log2(b))
    ans = 0
    for i in range(l + 1) :
        if (b & (1 << i)) != 0 :
            ans ^= (a << i)
            # print(a, i, a << i)
    return ans
def get_ans (n : int) -> int :
    ans = 0
    for a in range(n + 1) :
        for b in range(a, n + 1) :
            if xor_product(a, a) ^ xor_product(xor_product(2, a), b) ^ xor_product(b, b) == 5 :
                print(b//3)
                ans ^= b
    return ans

def solver (n: int) :
    a = [1, 2]
    ans = 0
    while 3 * a[-1] < n :
        a.append((2 * a[-1]) ^ a[-2])
    a.pop()
    for i in range(len(a)) :
        a[i] *= 3
    for x in a :
        ans ^= x
    print(ans, a)
    return ans

# a(n) = 2 * a(n - 1) ^ a(n - 2)
# print(ans)
# get_ans(10000) # 3, 6, 15, 24, 63

# 3, 6, 15, 24, 63, 102, 243, 384
# 1, 2, 5, 8, 21, 34, 81, 128
print(solver(10**18))
