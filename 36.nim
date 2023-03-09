import std/strutils
import std/math    
import std/bitops    
iterator `..`*[T](a: T, b: T): T =
  var res: T = a
  while res <= b:
    yield res
    inc res
proc is_palindrome (s: string):bool = 
    for i in 0..len(s) - 1 :
        if s[i] != s[len(s) - i - 1] :
            return false
    return true
proc to_binary_string (x:int):string = 
    var s = ""
    var powr = nextPowerOfTwo(x)
    if not isPowerOfTwo(x) :
        powr = powr div 2
    while powr != 0 :
        if (bitand(x, powr) != 0) :
            s = s & "1"
        else :
            s = s & "0"
        powr = powr div 2
    return s
var ans = 0
for i in 0..1000000 :
    let s = intToStr(i)
    let gamma = to_binary_string(i)
    if is_palindrome(s) and is_palindrome(gamma) :
        ans += i
echo ans
