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

const mx = 4097
var arr: array[mx, array[2, int]]
arr[0][0] = 0
arr[0][1] = 0
# arr[i][j][k] -> number of ways to get a sum of i such that # of bits written is 
for i in 1..mx - 1 :
    for j in 0..1 : # j = 0 means that Eric starts first; j = 1 means that Oscar starts first (who wins?)
        arr[i][j] = 1 - j
        for x in 1..i :
            if popcount(x) mod 2 == 1 :
                if arr[i - x][j] == 1 - j :  
                    arr[i][j] = j
            else : # now it's the other guy's turn
                if arr[i - x][1 - j] == j :
                    arr[i][j] = j
var win: array[mx, int]
var sum: array[mx, int]

var ans = 0
for i in 1..mx - 1 : # determine who wins with i
    if popcount(i) mod 2 == 0 :
        win[i] = arr[i][1]
    else :
        win[i] = 1 - arr[i][0]
    if win[i] == 0 :
        echo fmt"{i:b}"
        ans += i

sum[0] = 0
for i in 1..mx - 1 :
    sum[i] = sum[i - 1]
    if win[i] == 0 :
        sum[i] += i
    if popcount(i + 1) == 1 :
        echo sum[i]
# echo ans
var powr: array[20, clong]
powr[0] = 1
for i in 1..len(powr) - 1:
    powr[i] = powr[i - 1] * 2
var res: array[12, int]
echo res
res[1] = 1
for i in 2..11 :
    if i mod 2 == 0 :
        res[i] = res[i - 1] + powr[i] - 1
    else :
        res[i] = res[i - 1] * 2 + powr[i - 1 + ((i - 1) div 2)] - 2 * ((powr[i - 1] - 1) div 3) + (i div 2)
    echo res[i]
echo res

     
