def sumsq (n) :
    return (n * (n + 1) * (2 * n + 1))//6
def eval (x) :
    right = N//x
    left = N//(x + 1) + 1
    return (sumsq(right) - sumsq(left - 1)) * x
N = pow(10, 15)
MOD = pow(10, 9)
ans = 0
for i in range(1, N) :
    if i * i > N :
        break
    ans += eval(i) 
    ans %= MOD
    if N//i != i :
        ans += eval(N//i)
        ans %= MOD
print(ans % MOD)
