import numpy as np
def brute (starter, arr, n) :
    ind = 0
    tot = []
    while pow(4, ind) <= n :
        n -= pow(4, ind)
        tot.append(pow(4, ind))
        ind += 1
    if n != 0 :
        tot.append(n)
    ans = 0
    for i in range(len(tot)) :
        if tot[i] == pow(4, i) :
            ans += starter * tot[i] * tot[i]
            for j in range(i) :
                ans += (sum(arr) * pow(4, i + j))//len(arr)
        else :
            ans += starter * pow(4, i) * n
            for j in range(i) :
                complete_cycles = n//pow(4, j + 1)
                ans += (complete_cycles * sum(arr) * pow(4, 2 * j + 1))//len(arr)
                partial_cycles = n - complete_cycles * pow(4, j + 1)
                lengths = []
                for k in range(4) :
                    if partial_cycles >= pow(4, j) :
                        partial_cycles -= pow(4, j)
                        lengths.append(pow(4, j))
                    else :
                        lengths.append(partial_cycles)
                        partial_cycles = 0
                for k in range(4) :
                    ans += lengths[k] * arr[k] * pow(4, j)
    return ans
n = pow(10, 18)
mod = pow(10, 9) + 7

tot = 0
tot += brute(1, [0, 1, 2, 3], n)
tot += brute(2, [0, 2, 3, 1], n)
tot += brute(3, [0, 3, 1, 2], n)
print(tot % mod)
