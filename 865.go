package main

import (
	"fmt"
)

func main() {
	n := int(1e4)
	mod := int64(998244353)
	dp := make([][]int64, 2)
	for i := 0; i < len(dp); i++ {
		dp[i] = make([]int64, n)
	}
	dp[0][0] = 9
	ans := int64(9)
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
	fmt.Println(ans)
}
