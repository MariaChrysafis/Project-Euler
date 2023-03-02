using Primes
function pandigital(n::Int)::Bool
    mySet = Set(digits(n))
    if length(mySet) != length(digits(n))
        return false
    end
    for i in 1:length(digits(n))
       if !(i in mySet)
           return false
       end
    end
    return true
end
arr = []
for i in 1:10000000
    if i % 2 != 0 && pandigital(i) && isprime(i)
        push!(arr, i)
    end
end
println(findmax(arr))
