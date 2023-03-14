import bigints
import std/sequtils
import patty
import std/options
import std/math
import strutils
import std/algorithm
import std/sets
import tables
const WHITE: int = 40
const BLACK: int = 60
# dp[i][j][k][l]
# number of ways to group i white objects & j black objects
# such that
# each "grouping" is lexicographically smaller than (k, l)!
var dp: array[WHITE + 1, array[BLACK + 1, array[WHITE + 1, array[BLACK + 1, BigInt]]]]
for tot_white in 0..WHITE : # total white objects
  for tot_black in 0..BLACK : # total black objects
    for white in 0..WHITE : # white objects delta
      for black in 0..BLACK : # black objects delta
        if tot_black == 0 and tot_white == 0 :
          dp[tot_white][tot_black][white][black] = initBigInt(1)
          continue
        if white == 0 and black == 0 :
          dp[tot_white][tot_black][white][black] = initBigInt(0)
          continue
        var cnt = 1
        var prev_white = white
        var prev_black = black
        if black != 0 :
          prev_black -= 1
        else :
          prev_white = white - 1
          prev_black = BLACK
        dp[tot_white][tot_black][white][black] = dp[tot_white][tot_black][prev_white][prev_black]
        while cnt * white <= tot_white and cnt * black <= tot_black :
          dp[tot_white][tot_black][white][black] += dp[tot_white - cnt * white][tot_black - cnt * black][prev_white][prev_black]
          cnt += 1

echo dp[WHITE][BLACK][WHITE][BLACK]
