using Primes
function f(n::Int)
    val = 1
    for i in 1:n
        val = lcm(i, val)
    end
    return val
end
println(f(20))
