# Pari-GP again!
default(parisize, 1200000000000)
mx = 2
ind = 5
mat = matrix(mx,mx, i,j, if ((i == 1 && (j == mx || j == mx - 1)), Mod(1, 20092010), if (i == j + 1 && i != 0, Mod(1, 20092010), Mod(0, 20092010))))
v = vector(mx, i, Mod(1, 20092010))
m1 = (mat^(ind - 1))
vec = v * m1
