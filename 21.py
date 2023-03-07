ans = 0

def divisors (i) :
    d = 0
    for j in range(1, i) :
        if i % j == 0 :
            d += j
    return d


for i in range(2, 10001) :
    d = divisors(i)
    if i == divisors(d) and i != d :
        ans += i
print(ans)
