using Primes

function getter(N::Int128)
    ans::Int128 = 0
    for i in 1:floor(sqrt(N))
        ans += div(N, i)
    end
    ans *= 2
    gamma::Int128 = floor(sqrt(N))
    return ans - gamma * gamma
end

function f(N::Int128)
    ans::Int128 = 0
    for f::Int128 in 1:floor(sqrt(N))
        ans += totient(f) * getter(div(N, f * f))
    end
    return ans
end
base::Int128 = 10
println(f(base^15))
