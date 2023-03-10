import bigints
import std/sequtils
import patty
import std/options
import std/math
import strutils

const MOD: int = 1004535809
const MAX: int = 100

iterator `..`*[T](a: T, b: T): T =
  var res: T = a
  while res <= b:
    yield res
    inc res

proc is_prime (a:int):bool =
  if a <= 1 :
    return false
  for i in 2..a :
    if i * i > a :
      break
    if a mod i == 0 :
      return false
  return true
var mx = 0
var val = 0
for a in -1000..1000 :
  for b in -1000..1000 : # n^2 - a * n + b
    var n = 0
    while is_prime(n * n + a * n + b) :
      n += 1
    if mx < n :
      val = a * b
      mx = n
echo val
