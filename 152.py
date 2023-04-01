#!/bin/env python
import random
import math
from collections import defaultdict
from fractions import Fraction
# from sympy import Symbol, cos
def isprime (x) :
    for i in range(2, x) :
        if i * i > x :
            break
        if x % i == 0 :
            return False
    return True
class Solver :
    a = []
    s = defaultdict(lambda: 0)
    def __init__ (self, a) :
        print(len(a))
        self.a = a
        self.s = defaultdict(lambda: 0)
        for i in range(0, (1 << len(a))) :
            print(i)
            tot = Fraction(0, 1)
            for j in range(0, len(a)) :
                if (i & (1 << j)) != 0 :
                    tot += Fraction(1, a[j] * a[j])
            tot = reduce(tot)
            tup = (tot.numerator, tot.denominator) 
            self.s[tup] += 1
def reduce (a) :
    g = gcd(a.numerator, a.denominator)
    return Fraction(a.numerator//g, a.denominator//g)

def gcd (a, b) :
    if a == 0 or b == 0 :
        return max(a, b)
    return gcd(max(a, b) % min(a, b), min(a, b))

MX = 80

def okay (m) :
    pos = []
    for i in range(2, MX + 1) :
        if gcd(i, m) != 1 :
            pos.append(i)
    if m == 1 :
        print(pos)
    for i in range(1, (1 << len(pos))) :
        tot = []
        res = Fraction(0, 1)
        for j in range(0, len(pos)) :
            if (i & (1 << j)) != 0 :
                res = res + Fraction(1, pos[j] * pos[j])
                res = reduce(res)
                tot.append(pos[j])
        if gcd(res.denominator, m) == 1 :
            if m == 11 :
                print(res.numerator, res.denominator)
                print(tot)
            return True
    return False

fine = [True] * (MX + 1)
tot = [2, 3]
for i in range(4, MX + 1) :
    if isprime(i) and not okay(i) :
        print("NOT OKAY", i)
        for j in range(i, MX + 1, i) : 
            fine[j] = False
pos = []
for i in range(2, len(fine)) :
    if fine[i] :
        pos.append(i)
print(pos)
print(len(pos))

s1 = Solver(pos[:len(pos)//2])
b = pos[len(pos)//2:]
ans = 0
for i in range(0, (1 << len(b))) :
    tot = Fraction(0, 1)
    for j in range(0, len(b)) :
        if (i & (1 << j)) != 0 :
            tot += Fraction(1, b[j] * b[j])
    tot = Fraction(1, 2) - reduce(tot)
    tup = (tot.numerator, tot.denominator)
    ans += s1.s[tup]
print(ans)
