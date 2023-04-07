import math
def gcd (a, b) :
    if a == 0 or b == 0 :
        return max(a, b)
    return gcd(max(a, b) % min(a, b), min(a, b))
MX = 1234
mu = [0] * (MX + 1)
isprime = [True] * (MX + 1)
trace = [1] * (MX + 1)
for i in range(2, MX + 1) :
    trace[i] = i
    if isprime[i] :
        mu[i] = 1 - mu[i]
        j = 2 * i
        while j <= MX :
            isprime[j] = False
            mu[j] = 1 - mu[j]
            j += i
for i in range(2, MX + 1) :
    if i * i > MX :
        break
    j = i * i
    while j <= MX :
        while trace[j] % (i * i) == 0 :
            trace[j] = trace[j]//(i * i)
        j += i * i
print(trace[12])
for i in range(0, MX + 1) :
    if mu[i] == 0 :
        mu[i] = 1
    else :
        mu[i] = -1

for i in range(2, MX + 1) :
    if i * i > MX :
        break
    j = i * i
    while j <= MX :
        mu[j] = 0
        j += i * i

ans = 0
for g in range(1, MX + 1) :
    for g1 in range(1, MX//g + 1) :
        g_sq = math.isqrt((g * g1)//trace[g * g1]) * trace[g * g1]
        for i in range(1, (MX)//(g * g1) + 1) :
            ls = (i * g * g1)//g_sq
            if g_sq % 2 == 0 :
                ans += g * mu[g1] * ls
                continue
            else :
                if ls % 2 == 1 :
                    ans -= g * mu[g1]
                continue
            for j in range(1, ls + 1) :
                ans += g * mu[g1] * pow(-1, j * g_sq) 
print(ans)
