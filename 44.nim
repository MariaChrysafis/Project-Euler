import bigints
import std/sequtils
import patty
import std/options
import std/math
import strutils
import std/algorithm
import std/sets


const MAX = 10000

iterator `..`*[T](a: T, b: T): T =
  var res: T = a
  while res <= b:
    yield res
    inc res

var s = initHashSet[int]()
for i in 1..MAX - 1 :
  s.incl((i * (3 * i - 1)) div 2)
var ans = 100000000
for i in 1..MAX - 1 :
  for j in i + 1..MAX - 1 :
    let pi = (i * (3 * i - 1)) div 2
    let pj = (j * (3 * j - 1)) div 2
    if pj - pi >= ans :
      continue
    if s.contains(pi + pj) and s.contains(pj - pi) :
      echo $pi & " " & $pj
      ans = min(ans, pj - pi)
echo ans

