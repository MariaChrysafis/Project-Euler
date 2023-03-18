ans = 0
for (n = 2, 1000000, if ((n % 7 != 0), g = floor((3 * n)/7); ans = max(ans, g/n);));
ans
