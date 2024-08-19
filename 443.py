import math
import sys
def gcd (a: int, b: int) :
    if min(a, b) == 0 :
        return max(a, b)
    return gcd(max(a, b) % min(a, b), min(a, b));
class Main :
    def dfs (self, n) :
        if n in self.g :
            return self.g[n]
        if n == 4 :
            return 13
        self.g[n] = self.dfs(n - 1) + gcd(n, self.dfs(n - 1))
        return self.g[n]
    def __init__ (self) :
        self.g = dict()
sys.setrecursionlimit(100000)
main = Main()
# print(main.dfs(1000))
# for i in range(5, 13000) :
#     if gcd(i, main.dfs(i - 1)) != 1 :
#         print(i, main.dfs(i) - i)

prev = [[6,9]]
d = dict()
d[6] = 10
d[9] = 18
tot = [10, 18]
n = 10**15
for _ in range(100000) :
    p = prev[-1][-1]
    lower = 2 * p - 1
    upper = 2 * p - 1 + min(2 * int(math.sqrt(p) + 5), 10000000)
    if lower > n :
        break
    tot.append(2 * lower)
    arr = [lower]
    print(lower, upper)
    for i in range(lower + 1, upper + 1) :
        if gcd(tot[-1] - 1, i) != 1 :
            arr.append(i)
        tot.append(tot[-1] + gcd(tot[-1] - 1, i) - 1)
    prev.append(arr)
# print(math.log10(prev[-1][-1]))
# print(tot)
print(prev)
print(tot[-1] + n)
# print(prev)
# mx = 0
# n = 10**6
# for key, value in sorted(d.items()) :
#     if key <= n :
#         mx = max(mx, value)
# print(mx + n)
