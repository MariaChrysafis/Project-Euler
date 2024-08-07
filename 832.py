import numpy as np
class Solver :
    def step (self) :
        a = 1
        while a in self.pos :
            a += 1
        self.pos.add(a)
        b = 1
        while b in self.pos or a ^ b in self.pos :
            b += 1
        self.pos.add(b)
        self.pos.add(a ^ b)
        s = np.base_repr(a ^ b, 4)
        # print(s)
        # self.ans += pow(4, len(s) - 1)
        self.ans += (a ^ b) + a + b
    def __init__ (self) :
        self.pos = set()
        self.ans = 0

class Main :
    def solve (self) :
        for i in range(self.N) :
            self.solver.step()
        # print("ANSWER", self.solver.ans)
    def __init__ (self, N: int) :
        self.N = N
        self.solver = Solver()

def brute (starter, arr, n) :
    # print(starter, arr, n)
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
            # print(n, "guys of length", len(tot))
            ans += starter * pow(4, i) * n
            for j in range(i) :
                # how many complete cycles
                complete_cycles = n//pow(4, j + 1)
                ans += (complete_cycles * sum(arr) * pow(4, 2 * j + 1))//len(arr)
                # print(complete_cycles, "many complete cycles")
                partial_cycles = n - complete_cycles * pow(4, j + 1)
                # print(partial_cycles, "many partial cycles")
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
                # print(lengths)
                # print()
    # print(tot)
    return ans


    # for
n = pow(10, 18)
mod = pow(10, 9) + 7
# m1 = Main(n)
# m1.solve()

tot = 0
tot += brute(1, [0, 1, 2, 3], n)
tot += brute(2, [0, 2, 3, 1], n)
tot += brute(3, [0, 3, 1, 2], n)
print(tot % mod)
