p = [1, 1]
mod = 10**6
for _ in range(100000) :
    n = len(p)
    print("N:", n)
    p.append(0)
    for j in range(1, 100000) :
        jj = (j * (3 * j - 1))//2
        if jj > n :
            break
        p[n] += p[n - jj] * pow(-1, j + 1)
    for j in range(1, 100000) :
        jj = (j * (3 * j + 1))//2
        if jj > n :
            break
        p[n] += p[n - jj] * pow(-1, j + 1)
    p[n] %= mod
    if p[n] == 0 :
        print(n)
        exit()
print(p)
