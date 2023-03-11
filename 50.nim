import bigints
import std/sequtils
import patty
import std/options
import std/math
import strutils
import std/algorithm


const MOD: int = 1000000000
const MAX: int64 = 100

iterator `..`*[T](a: T, b: T): T =
  var res: T = a
  while res <= b:
    yield res
    inc res

var is_prime: array[1000000, bool]
for i in 0..len(is_prime) - 1 :
  is_prime[i] = true
is_prime[0] = false
is_prime[1] = false
var primes: seq[int]
for i in 2..len(is_prime) - 1 :
  if is_prime[i] :
    var j = 2 * i
    while j < len(is_prime) :
      is_prime[j] = false
      j += i
    primes.add(i)
var pref: seq[int]
pref.add(0)
for i in 0..len(primes) - 1 :
  pref.add(pref[len(pref) - 1] + primes[i])
var ans = 0
var ind = 0
for i in 0..len(primes) - 1 :
  for j in i..len(primes) - 1 :
    if pref[j] - pref[i] >= 1000000 :
      break
    if is_prime[pref[j] - pref[i]] :
      if ans < j - i :
        ans = j - i
        ind = pref[j] - pref[i]

echo ind
