using Primes
function factorial(n)
    global f = big(1)
    for i in 1:n
        f *= big(i)
    end
    println(sum(digits(f)))
end
factorial(100)
