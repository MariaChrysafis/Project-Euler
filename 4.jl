using Primes
function is_palindrome(x::Int)::Bool
    s = string(x)
    for i in 1:length(s)
        if s[i] != s[length(s) - i + 1]
            return false
        end
    end
    return true
end
a = []
for i in 100:999
    for j in 100:999
        if is_palindrome(i * j)
            push!(a, i * j)
        end
    end
end
println(findmax(a))
