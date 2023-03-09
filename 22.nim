import std/strutils
import std/algorithm    
iterator `..`*[T](a: T, b: T): T =
  var res: T = a
  while res <= b:
    yield res
    inc res
proc get_val (s:string):clong = 
    var ans: clong = 0
    for i in 0..len(s) - 1 :
        assert s[i] != '"'
        ans += int(s[i]) - int('A') + 1
    return ans
let f = open("names.txt")
let s = f.readLine()
var vec: seq[string]
vec.add("")
for i in 0..len(s) - 1:
    if s[i] == '"' :
        continue
    if s[i] == ',':
        vec.add("")
        continue
    add(vec[len(vec) - 1], s[i])
vec = sorted(vec, system.cmp[string])
var ans = 0
for i in 0..len(vec) - 1 :
    ans += (i + 1) * get_val(vec[i])
echo ans
