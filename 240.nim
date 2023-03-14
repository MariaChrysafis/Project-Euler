import bigints
import std/sequtils
import patty
import std/options
import std/math
import strutils
import std/algorithm
import std/sets
import tables
const DICE_SIDES: int = 12
const DICE_NUMBER: int = 20
const TOP_NUMBER: int = 70
var d: array[DICE_SIDES + 1, array[DICE_NUMBER + 1, array[DICE_SIDES * DICE_NUMBER + 1, BigInt]]]
var combo: array[DICE_NUMBER + 1, array[DICE_NUMBER + 1, BigInt]]
for i in 0..len(combo) - 1 :
  for j in 0..len(combo) - 1 :
    if i < j :
      combo[i][j] = initBigInt(0)
    elif j == 0 or i == j :
      combo[i][j] = initBigInt(1)
    else :
      combo[i][j] = combo[i - 1][j - 1] + combo[i - 1][j]
for a in 0..len(d) - 1 :
  for b in 0..len(d[0]) - 1 :
    for c in 0..len(d[0][0]) - 1 :
      # c is the sum of dices
      # a is the number of sides
      # b is the number of dice
      # d[number of sides][number of dices][sum of dice]
      if b == 0 and c == 0:
        d[a][b][c] = initBigInt(1)
        continue
      d[a][b][c] = initBigInt(0)
      for prev in 1..a :
        if b != 0 and c - prev >= 0 :
          d[a][b][c] += d[a][b - 1][c - prev]
var ans = initBigInt(0)
for tot in 70..DICE_SIDES * DICE_NUMBER : # tot is the total sum of dice (not just the top 10)
  for mx in 1..DICE_SIDES : # mx is the minimum top 10 value
    for a in 1..DICE_NUMBER : # a is how many times mx occurs
      for b in 1..min(a, 10) : # b is how many times mx occurs in the top 10
        if tot - 70 - mx * (a - b) < 0 or 10 - (a - b) < 0 or mx - 1 < 0:
          continue
        if DICE_SIDES - mx < 0 or 10 - b < 0 or 70 - b * mx - mx * (10 - b) < 0 :
          continue
        # we have a dice that show up as mx
        # we have b dice in the top 10 that show up as mx
        # we have a - b guys in the bottom 10 that show up as mx
        var left = d[mx - 1][10 - (a - b)][tot - 70 - mx * (a - b)] # bottom 10
        var right = d[DICE_SIDES - mx][10 - b][70 - b * mx - mx * (10 - b)] # top 10
        ans += left * right * combo[DICE_NUMBER][a] * combo[DICE_NUMBER - a][10 - b]

echo ans
