import bigints
import std/sequtils
import patty
import std/options
import std/math
import strutils
import std/algorithm
import std/sets


const MAX = 100

iterator `..`*[T](a: T, b: T): T =
  var res: T = a
  while res <= b:
    yield res
    inc res

# Idea:
# Let MX = 10^12. Suppose that we are trying to find S(MX)
# Let g(x, p) denote the number of numbers n <= MX/x such that all prime factors of n are >= p
# Claim: g(x, p) = g(x, p - 1) - g(x/p, p - 1)
# Desired result: sum [g(p, p) - g(p, p - 1)] * p

var is_prime: array[MAX + 1, bool]
var primes: seq[int]
for i in 0..len(is_prime) - 1 :
  is_prime[i] = true
is_prime[0] = false
is_prime[1] = false
for i in 2..len(is_prime) - 1 :
  if is_prime[i] :
    var j = 2 * i
    while j < len(is_prime) :
      is_prime[j] = false
      j += i
    primes.add(i)
var g: array[MAX + 1, seq[int]]
for x in 0..len(g) - 1 :
  g[x] = newSeq[int](len(primes))

for p in 0..len(g[0]) - 1 :
  for x in 1..len(g) - 1 :
    if p == 0 :
      g[x][p] = (MAX div x) - ((MAX div x) div primes[p])
    else :
      if x * primes[p] > MAX :
        g[x][p] = g[x][p - 1]
      else :
        g[x][p] = g[x][p - 1] - g[x * primes[p]][p - 1]
var ans = 0
for p in 0..len(primes) - 1 :
  if p != 0 :
    ans += (g[1][p - 1] - g[1][p]) * primes[p]
  else :
    ans += g[1][p] * primes[p]
echo ans



