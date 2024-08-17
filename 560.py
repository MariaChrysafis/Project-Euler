import copy
mod = int(1e9 + 7)
inv2 = (mod + 1)//2
def mex (arr: list) :
    s = set(arr)
    for i in range(1000000000000) :
        if i not in s :
            return i
def gcd(x: int, y: int):
    if min(x, y) == 0:
        return max(x, y)
    return gcd(max(x, y) % min(x, y), min(x, y))

def xor_convolution (a: list, b: list) -> list :
    m = len(a)
    c = [0] * m
    if m == 1 :
        c[0] = (a[0] * b[0]) % mod
        return c
    ap = []
    bp = []
    an = []
    bn = []
    for i in range(0, m//2) :
        ap.append((a[i] + a[i + m//2]) % mod)
        bp.append((b[i] + b[i + m // 2]) % mod)
    for i in range(0, m//2) :
        an.append((a[i] - a[i + m//2] + mod) % mod)
        bn.append((b[i] - b[i + m // 2] + mod) % mod)
    d0 = xor_convolution(ap, bp)
    d1 = xor_convolution(an, bn)
    for i in range(0, m//2) :
        c[i] = ((d0[i] + d1[i]) * inv2) % mod
        c[i + m//2] = ((d0[i] - d1[i] + mod) % mod * inv2) % mod
    return c

def power (a: list, b: int) -> list :
    ans = [0] * len(a)
    ans[0] = 1
    res = copy.copy(a)
    while b != 0 :
        print("T")
        if b % 2 == 1 :
            ans = xor_convolution(ans, res)
        res = xor_convolution(res, res)
        b //= 2
    return ans



class BruteForce:

    def number_theory (self) :
        self.lpf = []
        self.nim = []
        for i in range(self.n + 10) :
            self.lpf.append(i)
            self.nim.append(0)
        self.nim[1] = 1
        self.nim[2] = 0
        cnt = 2
        for i in range(2, len(self.lpf)) :
            # print(i)
            if self.lpf[i] == i :
                j = 2 * i
                while j < len(self.lpf) :
                    if self.lpf[j] == j :
                        self.lpf[j] = i
                    j += i
                if i > 2 :
                    self.nim[i] = cnt
                    cnt += 1
        for i in range(2, len(self.lpf)) :
            self.nim[i] = self.nim[self.lpf[i]]


    def __init__(self, n, k):
        self.n = n
        self.k = k
        self.d = dict()
        self.ans = 0
        self.number_theory()
        cnt = [0] * (2**20)
        for i in range(1, self.n) :
            # print(i, self.nim[i])
            cnt[self.nim[i]] += 1
        # print(cnt)
        # print(cnt)
        print(power(cnt, k)[0])
bf = BruteForce(int(10**7), int(10**7))
print(bf.ans)
