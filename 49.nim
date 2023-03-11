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

proc digits (x:int):seq[int] =
  var y = x
  var dig: seq[int]
  while y != 0 :
    add(dig, y mod 10)
    y = y div 10
  sort(dig)
  return dig


var is_prime: array[10000, bool]
for i in 0..len(is_prime) - 1 :
  is_prime[i] = true
is_prime[0] = false
is_prime[1] = false
for i in 2..len(is_prime) - 1 :
  var j = 2 * i
  while j < len(is_prime) :
    is_prime[j] = false
    j += i
for i in 1000..10000 - 1 :
  if not is_prime[i] :
    continue
  for j in i + 1..10000 - 1 :
    if not is_prime[j] :
      continue
    var k = 2 * j - i
    if k >= 10000 or k < 1000 :
      continue
    if not is_prime[k] :
      continue
    let di = digits(i)
    let dj = digits(j)
    let dk = digits(k)
    if di != dj or dj != dk :
      continue
    echo $i & " " & $j & " " & $k
