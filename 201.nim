import bigints
import std/sequtils
import patty
import std/options
import std/math
import strutils
import std/algorithm
import std/sets
import tables
const SET_SIZE = 100
const SET_TAKEN = 50
const SUM = (SET_SIZE * (SET_SIZE + 1) * (2 * SET_SIZE + 1)) div 6
var dp: array[SET_SIZE + 1, array[SET_TAKEN + 1, array[SUM + 1, int8]]]
for i in 0..SET_SIZE :
  echo i
  for j in 0..SET_TAKEN :
    for sum in 0..SUM - 1:
      dp[i][j][sum] = 0
      if j > i :
        continue
      if i == 0 :
        if sum == 0 :
          dp[i][j][sum] = 1
        continue
      if j == 0 :
        if sum == 0 :
          dp[i][j][sum] = 1
        continue
      dp[i][j][sum] = dp[i - 1][j][sum]
      if sum >= i * i :
        dp[i][j][sum] += dp[i - 1][j - 1][sum - i * i]
        dp[i][j][sum] = min(dp[i][j][sum], 3)
      # echo $i & " " & $j & " " & $sum & " " & $dp[i][j][sum]
var ans = 0
for i in 0..SUM :
  if dp[100][50][i] == 1 :
    echo i
    ans += i
echo ans
