# Simpler version of problem 581
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
mx = pow(10, 9)
okay = set()


def func(n, k):
    okay.add(n)
    if k == len(primes):
        return
    val = n
    while val <= mx:
        func(val, k + 1)
        val *= primes[k]


func(1, 0)
print(len(okay))
