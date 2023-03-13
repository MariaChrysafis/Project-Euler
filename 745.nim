import bigints
import std/sequtils
import patty
import std/options
import std/math
import strutils
import std/algorithm
import std/sets
import tables
iterator `..`*[T](a: T, b: T): T =
  var res: T = a
  while res <= b:
    yield res
    inc res
const MAX: int64 = 100000000000000
const MOD = (int)1e9 + 7
var a: array[10000000 + 1, int64]
var mu: array[10000000 + 1, int64]
var is_prime: array[10000000 + 1, bool]
for i in 0..len(mu) - 1 :
  mu[i] = 1
  is_prime[i] = true
is_prime[0] = false
is_prime[1] = false
for i in 2..len(mu) - 1 :
  if i * i >= len(mu) :
    break
  var j = i * i
  while j < len(mu) :
    mu[j] = 0
    j += i * i
for i in 2..len(mu) - 1 :
  if is_prime[i] :
    var j = i
    while j < len(is_prime) :
      is_prime[j] = false
      if mu[j] != 0 :
        mu[j] = - mu[j]
      j += i
var ans: int64 = 0
for i in 1..len(a) - 1 :
  a[i] = 0
  var j = i
  while j * j <= MAX :
    a[i] += ((MAX div (j * j)) mod MOD * (mu[j div i] + MOD) mod MOD) mod MOD
    a[i] = a[i] mod MOD
    j += i
  ans += ((a[i] * i) mod MOD * i) mod MOD
  ans = ans mod MOD
echo ans
