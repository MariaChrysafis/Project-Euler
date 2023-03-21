getter(k) = { mat = vector(10,i,0); g = k; while (g != 0,  mat[g % 10 + 1] += 1; g = floor(g / 10);); mat};
ans = 10^7
val  = -1
for (i = 2, 10^7, if ((getter(i) == getter(eulerphi(i))), if((i/eulerphi(i) < ans), ans = i/eulerphi(i); val = i;);));
print(val)
