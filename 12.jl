using Primes
function f(n)
    i::Int128 = 1
    while true
        i += 1
        triangle::Int128 = i * (i - 1)/2
        prod::Int128 = 1
        for (key, value) in factor(Dict, triangle)
            prod *= value + 1
        end
        if prod >= n
            return triangle
        end
    end
end
println(f(500))
