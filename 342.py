import copy
import math
import sys
from isCubed import isCubed
from sympy.ntheory import factorint
import sympy
import time


class Main :
    def generate_primes (self, x) :
        self.is_prime = [True] * (x + 1)
        self.is_prime[0] = self.is_prime[1] = True
        self.primes = []
        for i in range(2, x + 1) :
            if self.is_prime[i] :
                j = 2 * i
                while j < len(self.is_prime) :
                    self.is_prime[j] = False
                    j += i
                self.primes.append(i)

    def dfs (self, arr, n, x, phi, mx) :
        if x > mx :
            return
        if n == len(arr) :
            if isCubed(phi) :
                print(x * x, phi)
                self.ans += x
            return
        for powr in range(1, 10000) :
            if x * (arr[n]**(powr)) > mx :
                break
            self.dfs(arr, n + 1, x * (arr[n]**(powr)), phi * (arr[n]**((2 * powr - 1) % 3)) * (arr[n] - 1), mx)
        self.dfs(arr, n + 1, x, phi, mx)




    def __init__ (self, n: int) : # n = 10^10
        self.n = n
        self.generate_primes(int(math.sqrt(n)))
        self.ans = 0
        self.s = set()
        for i in range(len(self.primes)) :
            x = self.primes[i]
            print(x)
            for powr in range(2, 1000) :
                if x**(2 * powr) >= n * n :
                    continue
                self.tot = []
                prev = copy.copy(self.primes)
                prev = prev[:i]
                prev = prev[::-1]
                self.dfs(prev, 0, x**powr, (x - 1)*(x**(2 * powr - 1)), n)
        # self.tot = []
        # self.primes = self.primes[::-1]
        # self.dfs(0,1, 1, n * n)
        # print(self.ans)

N = 10**10
start_time = time.time()
sys.setrecursionlimit(15000)
main = Main(N)
print("--- %s seconds ---" % (time.time() - start_time))
print(main.ans)
print("--------------")
exit()
ans = 0
for i in range(2, N + 1) :
    t = sympy.totient(i * i)
    if isCubed(t) :
        print(i * i, sympy.totient(i * i), factorint(i))
        ans += i
print(ans)
