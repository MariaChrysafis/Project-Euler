# In order for T(n) = n * (n + 1)/2 to have all prime factors <= 47, we need both n and n + 1 to have all prime factors <= 47
# Say we look for all 47-smooth numbers <= mx, where mx = 10^13
# We know that each 47-smooth number is  a product of powers of one of the numbers in primes (2, 3, 5, 7, 11, ..., 47)
# So we can enumerate all 47-smooth numbers <= mx recursively (see func function) and put them into a set "okay"
# Now we just need to find how many n there are such that n is 47-smooth and n + 1 is 47-smooth, which is a trivial task once we find "okay"
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
mx = pow(10, 13)
okay = set()


def func(n, k):
    okay.add(n)
    if k == len(primes):
        return
    val = n
    while val <= mx:
        func(val, k + 1)
        val *= primes[k]


func(1, 0)
ans = 0
for i in okay:
    if i + 1 in okay:
        ans += i
print(ans)
