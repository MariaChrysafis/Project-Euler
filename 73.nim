import bigints
import std/sequtils
import patty
import std/options
import std/math
import strutils
import std/algorithm
import std/sets
import tables
const MX = 12000
var ans = 0
for i in 0..MX :
  for j in i + 1..MX : # 1/3 <= i / j <= 1/2
    if gcd(i, j) == 1 and 3 * i > j and 2 * i < j :
      ans += 1
echo ans
