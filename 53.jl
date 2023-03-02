using Primes
function f()
    ans = 0
    for i in 1:100
        for j in i:100
            if binomial(big(j), big(i)) > 1000000
                ans += 1
            end
        end
    end
    return ans
end
println(f())
