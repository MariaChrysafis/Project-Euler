ans = 0
for c in str(pow(2, 1000)) :
    ans += int(c) - int('0')
print(ans)
