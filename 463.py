d = dict()
e = dict()

def recursive_f (n) :
    if n in d :
        return d[n]
    if n % 2 == 0 :
        d[n] = recursive_f(n//2)
    if n % 4 == 1 :
        d[n] = 2 * recursive_f(n//2 + 1) - recursive_f(n//4)
    if n % 4 == 3 :
        d[n] = 3 * recursive_f(n//2) - 2 * recursive_f(n//4)
    return d[n]


def get_sum (n) :
    if n in e :
        return e[n]
    if n % 4 == 3 :
        e[n] = 6 * get_sum(n//2) - 8 * get_sum(n//4) - 1
    else :
        e[n] = get_sum(n - 1) + recursive_f(n)
    return e[n]


e[1] = 1
e[3] = 5
d[1] = 1
d[3] = 3
print(get_sum(pow(3, 37)))
