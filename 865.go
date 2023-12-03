package main

import (
	"fmt"
)

func main() {
	n := int(1e4)
	mod := int64(998244353)
	mult := func(x int64, y int64) int64 {
		return (x * y) % mod
	}
	binPow := func(x int64, y int64) int64 {
		res := x
		ans := int64(1)
		for y != 0 {
			if y%2 == 1 {
				ans = mult(ans, res)
			}
			res = mult(res, res)
			y /= 2
		}
		return ans
	}
	inv := func(x int64) int64 {
		return binPow(x, mod-2)
	}
	frac := func(x int64, y int64) int64 {
		return mult(x, inv(y))
	}
	dp := make([][]int64, 2)
	for i := 0; i < len(dp); i++ {
		dp[i] = make([]int64, n)
	}
	dp[0][0] = 10
	ans := int64(10)
	pref := make([]int64, len(dp[0])+1)
	for i := 5; i < n; i += 3 {
		pref[0] = 0
		for x := 0; x < len(dp[0]); x++ {
			pref[x+1] = pref[x] + dp[(i+1)%2][x]
			pref[x+1] %= mod
		}
		for j := 0; j < i; j++ {
			dp[i%2][j] = 0
			f := int64(9)
			if j == 0 {
				f = int64(10)
			}
			dp[i%2][j] = ((pref[n] - pref[max(j-2, 0)] + mod) % mod * f) % mod
			ans += dp[i%2][j]
			ans %= mod
		}
	}
	fmt.Println(mult(ans, frac(9, 10)))
}
