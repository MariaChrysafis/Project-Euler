iterator `..`*[T](a: T, b: T): T =
  var res: T = a
  while res <= b:
    yield res
    inc res

var is_prime: array[10000, bool]
for i in 0..len(is_prime) - 1 :
    is_prime[i] = true
is_prime[0] = false
is_prime[1] = false
for i in 2..len(is_prime) - 1 :
    if is_prime[i] :
        var j = 2 * i
        while j < len(is_prime) :
            is_prime[j] = false
            j += i
for i in 2..len(is_prime) - 1 :
    if is_prime[i] or i mod 2 == 0 :
        continue
    var fine: bool = false
    for x in 1..len(is_prime) :
        if x * x > len(is_prime) :
            break
        if i - 2 * x * x >= 0 and is_prime[i - 2 * x * x] :
            fine = true
    if not fine :
        echo i
