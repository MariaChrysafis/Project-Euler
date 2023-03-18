
MOD = 100000000
powr = 10^12 - 1
mat = matrix(4, 4, i, j, if((i - 1 == j), Mod(1, MOD), if((i == 1 && j <= 2), Mod(2, MOD), if((i == 1), Mod(3 * j - 11, MOD), Mod(0, MOD)))))
vec = matrix(4, 1, i, j, if((i == 3), Mod(1, MOD), Mod(16/2^i, MOD)))
ans = (mat^powr) * vec
