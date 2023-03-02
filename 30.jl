using Primes
arr = []
for i in 1:1000000
    dig = digits(i)
    p = []
    for x in dig
        push!(p, x ^ 5)
    end
    if sum(p) == i
        push!(arr, i)
    end
end
println(sum(arr) - 1)
