using Primes
function f(n)
    ans = 0
    for i in 1:n
        if isprime(i)
            ans += i
        end
    end
    ans
end
println(f(2000000))
