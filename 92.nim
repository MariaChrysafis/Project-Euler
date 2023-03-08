iterator `..`*[T](a: T, b: T): T =
  var res: T = a
  while res <= b:
    yield res
    inc res

import sets

proc f(val: int): int = 
  if val < 10 :
    return val * val
  return f(val div 10) + (val mod 10) * (val mod 10)

var arr: array[10000010, int]

proc last(val: int): int =
  if val == 89 or val == 1 :
    return val
  if arr[val] != 0 :
    return arr[val]
  var gamma = f(val)
  return last(gamma)

var ans = 0
for i in 1..10000000 :
  if last(i) == 89 :
    ans += 1

echo ans
