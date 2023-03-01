using Primes
function okay(a)
    s = string(a)
    for i in 0:length(s)
        left = "2"
        right = "2"
        if i >= 1
            left = s[i:length(s)]
        end
        if i + 1 <= length(s)
            right = s[1:i + 1]
        end
        if !isprime(parse(Int128, left)) || !isprime(parse(Int128, right))
            return false
        end
    end
    return true
end
function f()
    ans = 0
    for i in 10:1000000
        if okay(i) && isprime(i)
            ans += i
        end
    end
    println(ans)
end
f()
