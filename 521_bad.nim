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
iterator `...`*[T](a: T, b: T): T =
  var res: T = a
  while res >= b:
    yield res
    dec res
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
var cur: array[MAX + 1, int]
var prev: array[MAX + 1, int]
var ans = 0
for p in 0..len(primes) - 1 :
  prev = cur
  for x in MAX...1 :
    if p == 0 :
      cur[x] = (MAX div x) - ((MAX div x) div primes[p])
    else :
      if x * primes[p] > MAX :
        cur[x] = prev[x]
      else :
        cur[x] = prev[x] - prev[x * primes[p]]
  if p != 0 :
    ans += (prev[1] - cur[1]) * primes[p]
  else :
    ans += cur[1] * primes[p]
echo ans
