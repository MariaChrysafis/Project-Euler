
import itertools

M = pow(10, 13)
fib = [1, 2]
for i in itertools.count(start=2):
    fib.append(fib[len(fib) - 1] + fib[len(fib) - 2])
    if fib[i] > M:
        break


def cnt(cur_arr, x):
    if x < 0:
        return 0
    if len(cur_arr) == 0 or sum(cur_arr) <= x:
        return 1 << len(cur_arr)
    return cnt(cur_arr[:len(cur_arr)-1], x) + cnt(cur_arr[:len(cur_arr)-1], x - cur_arr[-1])


print(cnt(fib, pow(10, 13)))
