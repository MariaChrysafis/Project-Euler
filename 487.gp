f(n, k, p) = {
  res = 0;
  fact = List(Mod(1, p));
  for(i = 2, k + 10, listinsert(fact, fact[i - 1] * Mod(i - 1, p), #fact + 1););
  for(i = 1 , k + 1, res += Mod(-1, p)^(if(i == k, 1, 0)) * fact[k + 2]/fact[1 + i] * 1/fact[k + 2 - i] * (Mod(n, p)^i) * Mod(g[k + 2 - i], p););
  res = res/(k + 1);
  res
}
s(n, k, p) = {
  Mod(n + 1, p) * f(n, k, p) - f(n, k + 1, p)
}
ans = 0
g = List(bernfrac(0));
for(i = 1, 10^4 + 10, listinsert(g, bernfrac(i), #g + 1); print(i););
for (p=2*10^9, 2 * 10^9 + 2000, if(isprime(p), ans +=  lift(s(10^12, 10^4, p));););
ans
