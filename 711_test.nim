# Sequence for which Eric wins
import std/math
import std/bitops    
import strformat
import system    


iterator `..`*[T](a: T, b: T): T =
  var res: T = a
  while res <= b:
    yield res
    inc res

const modulo = 1000000007
proc mult (a:clong, b:clong):int = 
    return (a * b) mod modulo
proc plus (a:clong, b:clong):int = 
    return (a + b) mod modulo
proc binPow(x:clong, y:int):int = 
    var res = x
    var ans = 1
    var exp = y
    while exp > 0 :
        if exp mod 2 == 1 :
            ans = mult(ans, res)
        res = mult(res, res)
        exp = exp div 2
    return ans
proc inv (a: clong):int = 
    return binPow(a, modulo - 2)
proc divide (a:clong, b:clong):int = 
    return (mult(a, inv(b)))    
proc minus (a:clong, b:clong):int = 
    return (a mod modulo - b mod modulo + modulo) mod modulo
const mx = 12345678

var res: array[mx + 1, clong]
res[1] = 1
for i in 2..mx :
    if i mod 2 == 0 :
        res[i] = minus(plus(res[i - 1], binPow(2, i)), 1)
    else :
        res[i] = plus(minus(plus(mult(res[i - 1], 2), binPow(2, i - 1 + ((i - 1) div 2))), mult(divide((binPow(2, i - 1) - 1), 3), 2)), i div 2)
echo plus(res[len(res) - 1], binPow(2, mx))
