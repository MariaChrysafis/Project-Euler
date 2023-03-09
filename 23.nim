import std/sets
iterator `..`*[T](a: T, b: T): T =
  var res: T = a
  while res <= b:
    yield res
    inc res
var abundant: seq[int]
const mx = 28124    
var d: array[mx, int]
for i in 1..mx - 1 :
    var j = 2 * i
    while j < mx :
        d[j] += i
        j += i
for i in 1..mx - 1 :
    if d[i] > i :
        abundant.add(i)
var s = toHashSet([-1])
for x in abundant :
    for y in abundant :
        s.incl(x + y)
var ans = 0
for i in 1..mx :
    if not s.contains(i) :
        ans += i
echo ans
