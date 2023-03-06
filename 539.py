mod: int = 987654321

def add (x: int, y: int) :
    return (x % mod + y % mod) % mod

def mult (x: int, y:int) :
    return (x % mod * y % mod) % mod

def subtract (x: int, y: int) :
    return (x % mod - y % mod + mod) % mod

def sum_floor (n: int) -> int :
    if n == 1 :
        return 0
    if n % 2 == 0 :
        return add(sum_floor(n - 1), n//2)
    return mult((n//2), add(n//2, 1))

def S (n: int) -> int :
    if n % 2 == 0 :
        return add(S(n - 1), p(n))
    if n == 1 :
        return p(1)
    return subtract(mult(2, subtract(add(sum_floor(n), n), mult(2, S(n//2)))), 1)

def p (n:int) -> int:
    if n == 1 :
        return 1
    return mult(2, subtract(add(n//2, 1), p(n//2)))

print(S(1000000000000000000))
