using Primes
hexagonal = Set()
pentagonal = Set()
triangle = Set()
for i::Int64 in 1:100000
    push!(pentagonal, div(i * (3 * i - 1), 2))
    push!(hexagonal, i * (2 * i - 1))
    push!(triangle, div(i * (i - 1), 2))
    if div(i * (i + 1), 2) in pentagonal && div(i * (i + 1), 2) in hexagonal
        println(div(i * (i + 1), 2))
    end
end
