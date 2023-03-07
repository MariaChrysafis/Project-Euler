mx = 1001
ans = 0
for n in range(1, (mx + 1)//2 + 1) :
    ans += (2 * n - 1) * (2 * n - 1)
    ans += 4 * n * n - 6 * n + 3
    ans += 4 * (n - 1) * (n - 1) + 1
    ans += 4 * n * n - 10 * n + 7
print(ans - 3)
