package main

import "fmt"

func main() {
	mod := int64(987654319)
	mult := func(x int64, y int64) int64 {
		return (x * y) % mod
	}
	add := func(x int64, y int64) int64 {
		return (x + y) % mod
	}
	binPow := func(x int64, y int64) int64 {
		ans := int64(1)
		res := x
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
	n := 100
	fact := make([]int64, 0)
	fact = append(fact, 1)
	for i := 1; i <= n+10; i++ {
		fact = append(fact, mult(fact[len(fact)-1], int64(i)))
	}
	binom := func(x int64, y int64) int64 {
		return mult(fact[x], inv(mult(fact[y], fact[x-y])))
	}
	res := []int64{int64(1), int64(1)}
	for i := int64(2); i <= int64(n); i++ {
		res = append(res, 0)
		res[i] = 0
		for j := int64(0); j < i; j++ {
			res[i] = add(res[i], mult(mult(res[j], res[i-j-1]), binom(i-1, j)))
		}
		res[i] = mult(mult(i, 2*i-1), res[i])
	}
	fmt.Println(mult(res[n], inv(fact[n])))
}
