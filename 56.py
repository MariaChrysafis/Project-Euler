ans = 0
for a in range(0, 100) :
    for b in range(0, 100) :
        ans = max(ans, sum(list(map(int, str(pow(a, b)).strip()))))
print(ans)
