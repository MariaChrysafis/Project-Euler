using Primes
n = 100
a = []
b = []
for i in 1:n
    push!(a, i)
    push!(b, i * i)
end
println(-sum(b) + sum(a)^2)
