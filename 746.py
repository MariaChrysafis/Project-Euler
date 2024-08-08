import copy
import math

import numpy as np


class Main:
    def okay(self, s: str):
        for i in range(len(s)):
            if s[i] == '1':
                if s[(i + 1) % len(s)] == '1' or s[(i + 2) % len(s)] == '1' or s[(i + 3) % len(s)] == '1':
                    return False
        return True

    def chose(self, circle: int, x: int):
        ans = 0
        for i in range(0, pow(2, circle)):
            if bin(i).count("1") == x:
                s = bin(i)[2:]
                while len(s) < circle:
                    s = "0" + copy.copy(s)
                if self.okay(s):
                    ans += 1
        return ans

    def binPow(self, a: int, b: int) -> int:
        res = copy.copy(a)
        ans = 1
        powr = copy.copy(b)
        while powr > 0:
            if powr % 2 == 1:
                ans = self.mult(ans, res)
            res = self.mult(res, res)
            powr //= 2
        return ans

    def inv(self, a: int):
        return self.binPow(a, self.MOD - 2)

    def mult(self, a: int, b: int) -> int:
        return (a * b) % self.MOD

    def binom(self, a: int, b: int) -> int:
        assert a >= b
        return self.mult(self.fact[a], self.inv(self.mult(self.fact[b], self.fact[a - b])))

    def solver (self, N) :
        self.N = N
        ans = 0
        for i in range(N + 1):
            # print(i)
            ans += pow(-1, i) * self.mult(self.mult(self.binPow(4, i), self.actual(4 * N, i)),
                                          self.mult(self.mult(self.binom(N, i), self.fact[i]), self.brute(N - i)))
            if ans < 0:
                ans += self.MOD
            ans %= self.MOD
        return ans * 2
    def gen(self, circle: int, x: int):
        print("O1")
        self.dp = np.zeros((5, x + 2, circle + 3), dtype=int)
        # print("O2")
        self.dp[4][0][0] = 1
        for i in range(circle + 1):
            print(i)
            for j in range(x + 1):
                for k in range(len(self.dp)):
                    self.dp[k][j][i] %= self.MOD
                    if k >= 3:
                        self.dp[0][j + 1][i + 1] += self.dp[k][j][i]  # put something
                    self.dp[min(k + 1, len(self.dp) - 1)][j][i + 1] += self.dp[k][j][i]  # don't put anything
    def actual(self, circle: int, x: int):
        # ans = sum(self.dp[circle - 4][x])
        ans = 0
        for k in range(len(self.dp)) :
            ans += self.dp[k][x][circle - 4]
        for mask in [1, 2, 4, 8]:
            s = bin(mask)[2:]
            while len(s) < 4:
                s = "0" + s
            if s.count("1") > x:
                continue
            if s.count("1") > 1:
                continue
            ind = s.rfind("1")
            for k in range(ind):
                s += '0'
            # dp = self.dp[circle - len(s)][x - 1]
            for k in range(len(self.dp)):
                if k >= 3 - ind :
                    ans += self.dp[k][x - 1][circle - len(s)]
        return ans % self.MOD
    def brute(self, a: int) -> int:  # a is the number of families
        return (self.fact[2 * a] * self.fact[2 * a]) % self.MOD

    def __init__(self, N: int):
        self.N = N  # N is the number of families
        self.MOD = pow(10, 9) + 7
        self.fact = [1]
        for i in range(4 * self.N + 3):
            self.fact.append(self.mult(self.fact[-1], len(self.fact)))
        self.gen(4 * N + 4, N + 1)


def brute (circle: int, x: int) :
    def okay (s: str) :
        for i in range(len(s)) :
            if s[i] == '1' :
                for k in range(1, 4) :
                    if i + k < len(s) and s[i + k] == '1' :
                        return False
        return True

    ans = 0
    for i in range(0, pow(2, circle)):
        if bin(i).count("1") == x:
            s = bin(i)[2:]
            while len(s) < circle:
                s = "0" + copy.copy(s)
            if okay(s):
                ans += 1
    return ans

n = 2021
main = Main(n + 1)
ans = 0
for i in range(2, n + 1) :
    ans += main.solver(i)
    ans %= main.MOD
print(ans)
