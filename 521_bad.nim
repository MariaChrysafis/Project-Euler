import bigints
import std/sequtils
import patty
import std/options
import std/math
import strutils
import std/algorithm
import std/sets


const MAX: int64 = 100
const MOD: int64 = 1000000000

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
proc mult (a: int64, b: int64): int64 =
  return (a * b) mod MOD
proc add (a: int64, b: int64): int64 =
  return (a + b) mod MOD
proc sub (a: int64, b: int64): int64 =
  return (a - b + MOD) mod MOD
# Idea:
# Let MX = 10^12. Suppose that we are trying to find S(MX)
# Let g(x, p) denote the number of numbers n <= MX/x such that all prime factors of n are >= p
# Claim: g(x, p) = g(x, p - 1) - g(x/p, p - 1)
# Desired result: sum [g(p, p) - g(p, p - 1)] * p
const sq: int = 10
var is_prime: array[sq + 1, bool]
var primes: seq[int64]
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
var cur: array[MAX + 1, int64]
var cur_sum: array[MAX + 1, int64]
var prev: array[MAX + 1, int64]
var prev_sum: array[MAX + 1, int64]
var ans: int64 = 0
for p in 0..len(primes) - 1 :
  prev = cur
  prev_sum = cur_sum
  for x in MAX...1 :
    if p == 0 :
      cur[x] = (MAX div x) - ((MAX div x) div primes[p])
      var fl = MAX div x
      let fl2 = (fl div 2) mod MOD
      fl = fl mod MOD
      cur_sum[x] = (((fl * (fl + 1)) div 2) mod MOD - ((fl2 * (fl2 + 1))) mod MOD + MOD) mod MOD
    else :
      if x * primes[p] > len(cur) :
        cur[x] = prev[x]
        cur_sum[x] = prev_sum[x]
      else :
        cur[x] = sub(prev[x], prev[x * primes[p]])
        cur_sum[x] = sub(prev_sum[x], mult(prev_sum[x * primes[p]], primes[p]))
  if p != 0 :
    ans += mult(sub(prev[1], cur[1]), primes[p])
  else :
    ans += mult(cur[1], primes[p])
ans += cur_sum[1] - 1
echo ans
