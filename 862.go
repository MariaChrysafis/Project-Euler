package main

import "fmt"

func binom(arr []int) int64 {
	sum := 0
	for _, x := range arr {
		sum += x
	}
	if sum < 0 {
		fmt.Println("NOT OKAY")
	}
	ans := fact[sum]
	for _, x := range arr {
		ans /= fact[x]
	}
	return ans
}
func dfs(arr []int, tot int, cur int) {
	if cur == len(arr) {
		if tot != 0 {
			return
		}
		res := int64(0)
		for i := 1; i < 10; i++ {
			if arr[i] >= 1 {
				arr[i] -= 1
				res += binom(arr)
				arr[i] += 1
			}
		}
		fmt.Println(arr, res)
		total += (res) * (res - 1) / 2
		return
	}
	for cnt := 0; cnt <= tot; cnt++ {
		arr[cur] += cnt
		dfs(arr, tot-cnt, cur+1)
		arr[cur] -= cnt
	}
}

var fact = make([]int64, 30)
var total = int64(0)

func main() {
	fact[0] = 1
	for i := 1; i < len(fact); i++ {
		fact[i] = fact[i-1] * int64(i)
	}
	n := 12
	digits := 10
	dfs(make([]int, digits), n, 0)
	fmt.Println(total)
}
