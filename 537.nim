import bigints
import std/sequtils
import patty
import std/options
import std/math
import strutils

const MOD: int = 1004535809
const MAX: int = 20000

iterator `..`*[T](a: T, b: T): T =
  var res: T = a
  while res <= b:
    yield res
    inc res

proc mult (a:array[MAX + 1, int64], b:array[MAX + 1, int64]): array[MAX + 1, int64] =
  var c: array[MAX + 1, int64]
  for i in 0..len(a) - 1 :
    for j in 0..len(b) - 1 - i :
      c[i + j] += (a[i] * b[j]) mod MOD
      c[i + j] = c[i + j] mod MOD
  return c

proc binPow (a:array[MAX + 1, int64], powr: int): array[MAX + 1, int64] =
  var y = powr
  var res = a
  var ans: array[MAX + 1, int64]
  ans[0] = 1
  while y > 0 :
    if y mod 2 == 1 :
      ans = mult(ans, res)
    res = mult(res, res)
    y = y div 2
  return ans

var a: array[MAX + 1, int64]
var is_prime: array[15 * MAX + 1, bool]
for i in 0..len(is_prime) - 1 :
  is_prime[i] = true
for i in 2..len(is_prime) - 1 :
  if is_prime[i] :
    var j = 2 * i
    while j < len(is_prime) :
      is_prime[j] = false
      j += i

var pi = 0
for i in 2..len(is_prime) - 1 :
  if is_prime[i] :
    pi += 1
  if pi == len(a) :
    break
  a[pi] += 1
a[0] = 1
echo binPow(a, MAX)[MAX]
