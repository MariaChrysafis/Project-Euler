import bigints
import std/sequtils
import patty
import std/options
import std/math
import strutils

iterator `..`*[T](a: T, b: T): T =
  var res: T = a
  while res <= b:
    yield res
    inc res

const mx: int = 1000000
var is_prime: array[mx + 1, bool]
for i in 0..mx :
  is_prime[i] = true
is_prime[0] = false
is_prime[1] = false
for i in 2..mx :
  if is_prime[i] :
    var j = 2 * i
    while j < mx :
      is_prime[j] = false
      j += i
var ans = 0
for i in 2..mx :
  var fine: bool = true
  var cur = i
  for x in 1..len(intToStr(i)) :
    if cur mod 10 == 0 or not is_prime[cur]:
      fine = false
      break
    cur = cur div 10 + (cur mod 10) * (10 ^ (len(intToStr(i)) - 1))
  if fine :
    ans += 1
echo ans
