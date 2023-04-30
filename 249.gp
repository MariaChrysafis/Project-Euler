default(parisize, 1200000000)
p = Pol([Mod(1, 10^16)])
for (i = 1, 5000, if(isprime(i), p *= (1 + x^i););)
ans = 0
for (i = 1, 5000 * 5000, if(isprime(i), ans += polcoeff(p,i););)
ans
