import itertools
ans = 1
for x in list(itertools.permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])) :
    if ans == pow(10, 6) :
        print(''.join(map(str,x)))
        break
    ans += 1
