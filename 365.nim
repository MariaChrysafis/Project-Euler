import bigints
import std/sequtils
import patty
import std/options

iterator `..`*[T](a: T, b: T): T =
  var res: T = a
  while res <= b:
    yield res
    inc res
# Taken from RosettaCode
proc mulInv(a0, b0: int): int =
    var (a, b, x0) = (a0, b0, 0)
    result = 1
    if b == 1: return
    while a > 1:
        let q = a div b
        a = a mod b
        swap a, b
        result = result - q * x0
        swap x0, result
    if result < 0: result += b0

# Taken from Rosetta Code
proc chineseRemainder[T](n, a: T): int =
    var prod = 1
    var sum = 0
    for x in n:
        prod *= x
    for i in 0..<n.len:
        let p = prod div n[i]
        sum += a[i] * mulInv(p, n[i]) * p
    sum mod prod

proc get_digits (n:int64, p:int):seq[int64] =
    var vec: seq[int64]
    var m = n
    while m != 0 :
        vec.add(m mod p)
        m = (m - m mod p) div p
    return vec
const mx = 5001
var combo: array[mx, array[mx, BigInt]]
proc bigint_to_int(x:BigInt) : int64 =
    let gamma = toInt[int64](x)
    return gamma.get()
proc eval (n: int64, m: int64, p: int): int64 = # evaluate C(n, m) (mod p) using combinatorics class
    var ans: int64 = 1
    let left = get_digits(n, p)
    let right = get_digits(m, p)
    for i in 0..min(len(left), len(right)) - 1 :
        var left_val: int64 = left[i]
        var right_val: int64 = right[i]
        ans *= bigint_to_int(combo[left_val][right_val] mod initBigInt(p))
        ans = ans mod p
    return ans

for i in 0..(mx - 1) :
    for j in 0..(mx - 1) :
        if i < j :
            combo[i][j] = 0.initBigInt
        elif i == j or j == 0 :
            combo[i][j] = 1.initBigInt
        else :
            combo[i][j] = combo[i - 1][j] + combo[i - 1][j - 1]

var is_prime: array[mx, bool]
for i in 0..(mx - 1) :
    is_prime[i] = true
for i in 2..(mx - 1) :
    if is_prime[i] == true :
        var j = 2 * i
        while j < mx :
            is_prime[j] = false
            j += i
var a: seq[int]
var left = 1000
var right = 5000
for i in left..right :
    if is_prime[i] :
        add(a, i)
var b: seq[int]
for i in 0..len(a) - 1:
    add(b, int(eval(1000000000000000000, 1000000000, a[i])))
var ans = 0
for p in 0..len(a) - 1:
    for q in p + 1..len(a) - 1:
        for r in q + 1..len(a) - 1:
            let p1 = b[p]
            let q1 = b[q]
            let r1 = b[r]
            let val = chineseRemainder([a[p], a[q], a[r]], [b[p], b[q], b[r]])
            ans += val
echo ans
