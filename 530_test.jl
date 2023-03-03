using Primes
function moebius(n::Integer)
    @assert n > 0
    m(p, e) = p == 0 ? 0 : e == 1 ? -1 : 0
    reduce(*, m(p, e) for (p, e) in factor(n) if p ≥ 0; init=1)
end
μ(n) = moebius(n)
function f(n::Int)::Int
    ans = 0
    for j in 1:n
        if n % j == 0
            ans += gcd(j, div(n, j))
        end
    end
    return ans
end
function F(n::Int)::Int
    ans = 0
    for i in 1:n
        ans += f(i)
    end
    return ans
end
function F_fast(N::Int)
    ans = 0
    gamma::Int = floor(sqrt(N))
    arr::Array{Int} = zeros(gamma + 1)
    for i in 1:N
        arr[1] += div(N, i)
    end

    for x in 2:gamma
        n = div(N, x)
        for val in 1:div(N, x * x)
            arr[x] += div(div(n, x), val)
        end
    end

    println(arr)

    new_arr::Array{Int} = zeros(gamma + 1)
    for i in 1:gamma
        d = i
        while d <= length(arr)
            new_arr[i] += arr[d] * µ(div(d, i))
            d += i
        end
    end
    res = 0
    for i in 1:length(new_arr)
        res += new_arr[i] * i
    end
    println(res)
end
println(F(1000))
F_fast(1000)
