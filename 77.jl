using Primes
function f(n)
    dp = zeros(Int128, n, n)
    # dp[i][j] is the number of ways to get a sum of i with primes <= j
    for i in 1: n
        for j in 1: n
            dp[i, j] = dp[i, j - 1] # does not contain j
            if (!isprime(j))
                 continue
            end
            k = j
            while k <= i # contains j k/j times
                if (i != k)
                     dp[i, j] += dp[i - k, j - 1]
                else
                     dp[i, j] += 1
                end
                k += j
            end
        end
        if dp[i, i + 1] >= 5000
            return i
        end
    end
end
println(f(100))
