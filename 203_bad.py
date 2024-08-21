def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m
def mult (a, b, m) :
    return (a * b) % m
import math
mx = 10**4
l = 0
r = mx
while l != r :
  m = (l + r)//2
  if math.floor(m * (1 + math.sqrt(5))/2) > mx :
      r = m
  else :
      l = m + 1
golden = (1 + math.sqrt(5))/2
pp = 7**10
qq = math.floor(pp/golden)
res = l
ans = - mx * (mx + 1) * (mx + 2)//6 * 3 + mx * (mx + 1)//2 * (mx - res + 1)
ans += (mx * (mx + 1)//2 - (res - 1) * res//2) * (mx + 1)
ans += res * (res - 1)//2
mod = 7**9
tot = 0
for i in range(1, res) :
   tot -= ((i * pp) % qq) * i
intermediate = (tot * modinv(qq, mod)) % mod
ans += intermediate
tot = 0
for i in range(1, res) :
   tot -= (i * pp) % qq * qq
   tot += ((i * pp) % qq)**2
res = (tot * modinv(2 * qq * qq, mod)) % mod
ans += res
# ans += tot//(2 * qq*qq)
assert ans % mod == 230312207313 % mod
q = 7**10
while q <= 7**10 :
  p = math.floor(q * (1 + math.sqrt(5))/2)
  for p in range(p, p + 2) :
      if abs((1 + math.sqrt(5))/2 - p/q) >= 0 :
          print(p, q, abs((1 + math.sqrt(5))/2 - p/q))
  q *= 7









