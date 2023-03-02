using Primes
arr = []
for i in 1:1000
    push!(arr, powermod(big(i), i, big(10)^big(10)))
end
println(sum(arr) % big(10) ^ big(10))
