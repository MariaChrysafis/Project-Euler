using Primes
function main()
    mod::Int128 = 1e9 + 7
    dict = Dict()
    dict[1] = 1
    function S(N::Int128)
        if haskey(dict, N)
            return dict[N]
        end
        ans::Int128 = div((N) * (N + 1), 2)
        for m in 2:N
            if m * m > N
                break
            end
            ans += mod - S(div(N, m))
            ans %= mod;
        end
        for d in 1:N
            if d * d >= N
                break
            end
            if d == div(N, d)
                continue
            end
            ans += mod - ((div(N, d) - div(N, d + 1)) * S(d)) % mod
            ans %= mod
        end
        dict[N] = ans
        return ans
    end
    N::Int128 = 10^11
    i = 2
    res = 0
    while i <= N
        println(i)
        res += S(div(N, i))
        res += mod - 1
        res %= mod
        i *= 2
    end
    println(res)
end
main()
