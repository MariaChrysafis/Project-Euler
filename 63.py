ans = 0
for n in range(100) :
    for x in range(1000) :
        res = pow(x, n)
        if len(str(res)) > n :
            continue
        if len(str(res)) == n :
            print(res, n)
            ans += 1
print(ans - 1)
