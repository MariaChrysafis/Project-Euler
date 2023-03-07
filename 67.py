sz = 100
arr = []
for i in range(0, sz) :
    arr.append(list(map(int, input().strip().split())))

dp = []
for i in range(0, sz) :
    dp.append([0] * sz)

for i in range(0, sz) :
    for j in range(0, i + 1) :
        if i == 0 and j == 0 :
            dp[i][j] = arr[i][j]
            continue
        if i != 0 :
            dp[i][j] = max(dp[i][j], dp[i - 1][j] + arr[i][j])
        if j != 0 and i != 0 :
            dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + arr[i][j])

print(max(dp[-1]))
