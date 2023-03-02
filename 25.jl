using Primes
function fibonacci(n)
   fib = BigInt[1 1; 1 0]^n
   return fib[2, 1]
end
function f(dig)
    l = 0
    r = 5000
    while l != r
        m = (l + r) ÷ 2
        if length(digits(fibonacci(m))) >= dig
            r = m
        else
            l = m + 1
        end
    end
    return l
end
println(f(1000))
