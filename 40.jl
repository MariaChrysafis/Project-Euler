using Primes
function f(N::Int)
    s::String = ""
    v::Vector{Char} = []
    for i in 1:N
        for c in string(i)
            push!(v, c)
        end
        if length(v) >= N
            return Int(v[N]) - Int('0')
        end
    end
end
println(f(10) * f(100) * f(1000)* f(10000) * f(100000) * f(1000000))
