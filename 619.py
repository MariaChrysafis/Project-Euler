import random

import numpy as np
l = 1000000
r = 1234567
lpf = []
primes = []
to_index = dict()
def smaller (x: list, y: list) :
    if len(x) < len(y) :
        return True
    if len(x) > len(y) :
        return False
    return x < y
def desquare (x: int) -> int :
    for i in range(2, x + 1) :
        if i * i > x :
            return x
        if x % (i * i) == 0 :
            x //= (i * i)
    return x

def xor (s1: list, s2: list) :
    s = []
    d = dict()
    for x in s1 :
        if x not in d :
            d[x] = 0
        d[x] += 1
    for x in s2 :
        if x not in d :
            d[x] = 0
        d[x] += 1
    for key, value in d.items() :
        if value % 2 == 1 :
            s.append(key)
    return sorted(s)
def factorization (x: int) :
    global lpf
    d = dict()
    while x != 1 :
        if lpf[x] not in d :
            d[lpf[x]] = 0
        d[lpf[x]] += 1
        x //= lpf[x]
    return d
def main() :
    global lpf
    global primes
    for i in range(r + 1) :
        lpf.append(i)
    for i in range(2, r + 1) :
        j = i
        if lpf[i] == i :
            while j + i <= r :
                j += i
                lpf[j] = i
            to_index[i] = len(primes)
            primes.append(i)
    strings = []
    for i in range(l, r + 1) :
        d = factorization(i)
        ans = 1
        fine = True
        s = []
        for key, value in d.items() :
            if i - key < l and key + i > r :
                fine = False
            if value % 2 == 1 :
                ans *= key
                s.append(key)
        if not fine :
            continue
        strings.append(sorted(s))
    for ind in range(5) :
        # print(ind)
        strings = sorted(strings)
        for j in range(1, len(strings)) :
            if len(strings[j]) == 1 :
                for x in range(j + 1, len(strings)) :
                    if strings[j][0] in strings[x] :
                        strings[x].remove(strings[j][0])
                    else :
                        break
        strings = sorted(strings)
        for j in range(1, len(strings)) :
            t1 = strings[j - 1]
            t2 = strings[j]
            t = xor(t1, t2)
            if smaller(t, t2) :
                strings[j] = t
            elif smaller(t, t1) :
                strings[j - 1] = t2
                strings[j] = t
        strings = sorted(strings)
    ans = 1
    for x in strings :
        # print(x)
        if len(x) == 0 :
           ans *= 2
           ans %= (int(1e9 + 7))
    print(ans - 1)


main()
